# Create your views here.
import json
from django.shortcuts import *
from django.template import RequestContext
from forum.forms import CommentForm

def PostComment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)

        message = 'something wrong!'
        if(form.is_valid()):
            print(request.POST['title'])
            message = request.POST['title']

        return HttpResponse(json.dumps({'message': message}))

    return render_to_response('forum/comment.html',
            {'form':CommentForm()}, RequestContext(request))