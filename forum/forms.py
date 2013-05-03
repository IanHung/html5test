'''
Created on 2013-05-03

@author: Ian
'''
from forum.models import Comment
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        
