# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from forum.forms import CommentForm

def PostComment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(request.POST)
        message = 'something wrong!'
        if(form.is_valid()):
            print(form)
            form.save()

        return HttpResponse(json.dumps({'message': message}))

    return render(request, 'forum/comment.html',
            {'form':CommentForm()})