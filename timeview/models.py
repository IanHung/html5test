from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Timelike(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, blank=True, null=True)
    localsource = models.FileField(upload_to='video/timelike', blank=True)
    youtubesource = models.URLField(max_length=200, blank=True)
    vimeosource = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    
    def clean(self):
        from django.core.exceptions import ValidationError
        #allow only one source for video/audio
        
        if (int(not self.localsource) + int(not self.youtubesource) + int(not self.vimeosource)) != 2:
            raise ValidationError('Please select exactly one source for the video')
        