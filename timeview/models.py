from django.db import models

# Create your models here.
class Timelike(models.Model):
    title = models.CharField(max_length=200)
    localsource = models.FilePathField(null=True)
    youtubesource = models.URLField(max_length=200)
    
    