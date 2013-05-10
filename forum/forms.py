'''
Created on 2013-05-03

@author: Ian
'''
from forum.models import Comment
from django import forms
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
             'comment': forms.TextInput(attrs={'class': 'span5 comment'}),      
        }

        
