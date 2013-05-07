# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from timeview.models import Timelike
from django.contrib.contenttypes.models import ContentType
from forum.forms import CommentForm

def index(request):
    timelike_list = Timelike.objects.order_by('title')
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        print(commentform)
        print(request.POST)
        message = 'something wrong!'
        if(commentform.is_valid()):
            print(commentform.is_valid())
            comment=commentform.save(commit=False)
            comment.end=request.POST['end']
            comment.start=request.POST['start']
            comment.title=request.POST['title']
            comment.object_id=request.POST['object_id']
            comment.content_type=ContentType.objects.get_for_model(Timelike)
            comment.isBasic=request.POST['isBasic']
            comment.save()
    
        return HttpResponse(json.dumps({'message': message}))
    
    return render(request, 'timeview/time.html', {'timelike_list': timelike_list, 'form':CommentForm()})