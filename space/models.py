from django.db import models
from django.contrib.auth.models import User
from forum.models import Comment
from django.contrib.contenttypes import generic
from basePages.models import Article

# Create your models here.
class Paragraph(models.Model):
    #basic fields
    article = models.ForeignKey(Article, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    content = models.TextField(blank=True)
    comment = generic.GenericRelation(Comment)
    
    class Meta:
        unique_together = ('article','position')
    
    def __str__(self):
        return 'test paragraph'

    def save(self):
        super(Paragraph, self).save()
        earlier = Paragraph.objects.filter(article=self.article).exclude(id=self.id).order_by('-position')
        earlier1 = ImageClass.objects.filter(article=self.article).order_by('-position')
        if (earlier != earlier1):
            if (earlier):
                self.position = earlier[0].position+1
            elif (earlier1):
                self.position = earlier1[0].position+1
        elif (earlier and earlier1):
            self.position = max(earlier[0].position, earlier1[0].position)+1
        else:
            self.position = 0 
        super(Paragraph, self).save()


class ImageClass(models.Model):
    #basic fields
    article = models.ForeignKey(Article, blank=True, null=True)
    position = models.PositiveIntegerField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    comment = generic.GenericRelation(Comment)
    localsource = models.FileField(upload_to='image/spacelike', blank=True)
    linksource = models.URLField(max_length=200, blank=True)
    imagetype = models.PositiveSmallIntegerField(blank=True, null=True)
        
    class Meta:
        unique_together = ('article','position')
    
    def __str__(self):
       return 'test image'

    def save(self):
        super(ImageClass, self).save()
        earlier = Paragraph.objects.filter(article=self.article).order_by('-position')
        earlier1 = ImageClass.objects.filter(article=self.article).exclude(id=self.id).order_by('-position')
        if (earlier != earlier1):
            if (earlier):
                self.position = earlier[0].position+1
            elif (earlier1):
                self.position = earlier1[0].position+1
        elif (earlier and earlier1):
            self.position = max(earlier[0].position, earlier1[0].position)+1
        else:
            self.position = 0 
        super(ImageClass, self).save()
