from django.db import models
from django.contrib.auth.models import User
from forum.models import Comment
from django.contrib.contenttypes import generic


# Create your models here.
class Timelike(models.Model):
    #basic fields
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True, null=True)
    localsource = models.FileField(upload_to='video/timelike', blank=True)
    youtubesource = models.URLField(max_length=200, blank=True)
    vimeosource = models.URLField(max_length=200, blank=True)
    #adding relationship to Comment class
    comment = generic.GenericRelation(Comment)
    
    
    def __str__(self):
        return self.title
    
    def clean(self):
        from django.core.exceptions import ValidationError
        #allow only one source for video/audio
        
        if (int(not self.localsource) + int(not self.youtubesource) + int(not self.vimeosource)) != 2:
            raise ValidationError('Please select exactly one source for the video')
        