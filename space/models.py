from django.db import models
from django.contrib.auth.models import User
from forum.models import Comment
from django.contrib.contenttypes import generic

# Create your models here.
class Paragraph(models.Model):
    #basic fields
    author = models.ForeignKey(User, blank=True, null=True)
    comment = generic.GenericRelation(Comment)

class Imageclass(models.Model):
    #basic fields
    author = models.ForeignKey(User, blank=True, null=True)
    comment = generic.GenericRelation(Comment)
    localsource = models.FileField(upload_to='image/spacelike', blank=True)
    linksource = models.URLField(max_length=200, blank=True) 
    
def __str__(self):
    return self.title
