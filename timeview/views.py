# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from timeview.models import Timelike
from forum.forms import CommentForm

def index(request):
    timelike_list = Timelike.objects.order_by('title')
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(request.POST)
        message = 'something wrong!'
        if(form.is_valid()):
            print("sick")
            
    
        return HttpResponse(json.dumps({'message': message}))
    
    return render(request, 'timeview/time.html', {'timelike_list': timelike_list, 'form':CommentForm()})