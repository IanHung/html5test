# Create your views here.
from django.shortcuts import render
from timeview.models import Timelike

def index(request):
    timelike_list = Timelike.objects.order_by('title')
    return render(request, 'timeview/time.html', {'timelike_list': timelike_list})