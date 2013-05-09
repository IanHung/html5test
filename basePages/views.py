# Create your views here.
import json
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'basePages/home.html')

def generalLogin(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    message = {'user': 'Failed to Log in', 'worked': False}
    if user is not None:
        if user.is_active:
            login(request, user)
            message = {'user': username, 'worked': True}
            return HttpResponse(json.dumps(message))
            
    else:
        return HttpResponse(json.dumps(message))
        
def generalLogout(request):
    print(request.POST)
    logout(request)
    message = {'complete': 'complete'}
    return HttpResponse(json.dumps(message))
    
        