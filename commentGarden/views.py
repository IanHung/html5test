# Create your views here.

from django.shortcuts import render
from basePages.models import SubjectStream
from forum.forms import CommentForm


def index(request):
    comment_list = SubjectStream.objects.order_by('id')
       
    return render(request, 'commentGarden/commentgarden.html', {'comment_list': comment_list, 'form':CommentForm()})