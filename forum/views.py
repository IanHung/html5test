# Create your views here.

import json
from forum.models import Comment
from django.contrib.contenttypes.models import ContentType
from forum.forms import CommentForm
from timeview.models import Timelike
from django.shortcuts import HttpResponse

def PostComment(request):
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
        if (request.POST['isBasic']=='on'):
            comment.isBasic=True
        else:
            comment.isBasic=False
        comment.save()
        newComment = Comment.objects.latest('pubDate')
        message = newComment.singlejson()
        print(message)
    return HttpResponse(json.dumps(message))