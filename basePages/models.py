from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
#Article Class each update.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, blank=True)
    author = models.ForeignKey(User, blank=True, null=True)
    pubDate = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()
    viewcount = models.PositiveIntegerField()
    subjectStream = models.ForeignKey('SubjectStream', null=True)
    abstract = models.TextField(null=True)
    
    def __str__(self):
        return '%i %i %i %s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, self.title)
    
    def generateRelated(self):
        return False
    
    #Creating slug.
    def save(self):
        super(Article, self).save()
        self.slug = '%i/%i/%i/%s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, slugify(self.title))
        super(Article, self).save()

#class to manage the updating of each article    
class ChangeLog(models.Model):
    lastEdited = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)
    
    def __str__(self):
        return '%i %i %i %s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, self.article.title)

#class to manage the subject tags.
class Tag(models.Model):
    subject = models.CharField(max_length=200)
    
    def __str__(self):
        return self.subject
    
#class subject stream listing every article in a subject.
class SubjectStream(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User, blank=True, null=True)
    pubDate = models.DateTimeField(auto_now_add=True)
    abstract = models.TextField(null=True)
   
    def __str__(self):
        return '%i %i %i %s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, self.title)
    
    def save(self):
        super(SubjectStream, self).save()
        self.slug = '%i/%i/%i/%s' % (self.pubDate.year, self.pubDate.month, self.pubDate.day, slugify(self.title))
        super(SubjectStream, self).save()

#PositionInArticle Helper class add to all objects that can be in an article.        
class PositionInArticle(models.Model):
    article = models.ForeignKey(Article)
    position = models.PositiveIntegerField()
    
    class Meta:
        unique_together = ('article','position')
        
    
    
    