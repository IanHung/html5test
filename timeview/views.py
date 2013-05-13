# Create your views here.

from django.shortcuts import render
from timeview.models import Timelike
from forum.forms import CommentForm


def index(request):
    timelike_list = Timelike.objects.order_by('-pubDate', '-id')
       
    return render(request, 'timeview/time.html', {'timelike_list': timelike_list, 'form':CommentForm()})