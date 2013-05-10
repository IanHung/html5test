from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# Create your models here.
class Comment(models.Model):
    #basic requirements for comment objects
    title = models.CharField(max_length=200)
    pubDate = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True)
    comment = models.TextField()
    #setting up relationships for multiple model types
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    #need to create a smarter object id that would work across object types.
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    #Need to add relations to other models classes.
    comments = generic.GenericRelation('self')
    #start anchor and end anchor (end possibly not needed). Actually depends on type.
    start = models.FloatField(blank=True)
    end = models.FloatField(blank=True)
    #Enrichment comment or just a basic comment.
    isBasic = models.BooleanField()
  
    def __str__(self):
        return self.title

    #added a method that will allow me to limit the number of comments that can appear at once, where num is the number of comments that appear.
    #I should probably make this a filter instead of a method. 
    def get_later_start(self):
        num = 1
        later = Comment.objects.filter(isBasic=True,content_type=self.content_type, object_id=self.object_id ,start__gt=self.start).order_by('start')
        if later:
            return max(min(later[num-1].start, self.end), self.start +1)
        return False
    
    def get_earlier_id(self):
        later = Comment.objects.filter(isBasic=True,content_type=self.content_type, object_id=self.object_id ,start__lte=self.start).exclude(id=self.id).order_by('-start')
        if later:
            return later[0].id
        return self.id
    
    def singlejson(self):
        #need to set up user login 'author' : self.author.username, need to do something with pubdate 'pubDate' : self.pubDate,
        sjson = {'id' : self.id, 'title' : self.title, 'comment' : self.comment, 'content_type' : self.content_type.name, 'object_id' : self.object_id, 'start' : self.start, 'end' : self.end, 'isBasic' : self.isBasic, 'previd' : self.get_earlier_id()}
        return sjson
    
    class Meta:
        ordering = ["-start"]
#admin class for posters
