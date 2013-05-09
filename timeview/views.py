# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from timeview.models import Timelike
from forum.models import Comment
from django.contrib.contenttypes.models import ContentType
from forum.forms import CommentForm


def index(request):
    timelike_list = Timelike.objects.order_by('-pubDate', '-id')
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        message = {'message': 'something wrong!'} 
        print(request.POST)
        if(commentform.is_valid()):
            comment=commentform.save(commit=False)
            if request.user.is_authenticated():
                comment.author = request.user
            comment.end=request.POST['end']
            comment.start=request.POST['start']
            comment.title=request.POST['title']
            comment.object_id=request.POST['object_id']
            comment.content_type=ContentType.objects.get_for_model(Timelike)
            comment.isBasic=request.POST['isBasic']
            comment.save()
            newComment = Comment.objects.latest('pubDate')
            message = newComment.singlejson()
            print(message)
        return HttpResponse(json.dumps(message))
    
    return render(request, 'timeview/time.html', {'timelike_list': timelike_list, 'form':CommentForm()})