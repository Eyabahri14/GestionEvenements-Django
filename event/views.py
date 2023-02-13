from django.shortcuts import render
from .models import Event

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello world")


def list_event(request):

    list = Event.objects.all()

    context = {'l' : list}

    return render (request, 'event/list_event.html', context)
