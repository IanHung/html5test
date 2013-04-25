from django.db import models

# Create your models here.
class Timelike(models.Model):
    source = models.FilePathField()
    