'''
Created on 2013-05-13

@author: Ian
'''
from django.contrib import admin
from basePages.models import Article, ChangeLog, Tag, SubjectStream, PositionInArticle

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    
class SubjectStreamAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ChangeLog)
admin.site.register(Tag)
admin.site.register(SubjectStream, SubjectStreamAdmin)
admin.site.register(PositionInArticle)
