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
    start = models.PositiveIntegerField(blank=True)
    end = models.PositiveIntegerField(blank=True)
  

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-start"]
