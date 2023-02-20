from django.shortcuts import render
from .models import Event
from django.views.generic import *
from .forms import EvenementForm
from django.urls import reverse_lazy

from django.http import HttpResponse
# Create your views here.

def index(request , name):

    text = f"Hello {name}"
    return HttpResponse(text)


def list_event(request):

    list = Event.objects.filter(state=True).order_by('evt_date')

    Nbr = Event.objects.count()

    context = {'events' : list  , "nombre" : Nbr}

    return render (request, 'event/list_event.html', context)


class ListEvents(ListView):

    model = Event
    template_name = "event/list_event.html"
    context_object_name = "events"  # par défaut object_list
    
    def get_queryset(self):
        eventsTrue = Event.objects.filter(state=True).order_by('evt_date')
        return  eventsTrue
    

class AddEvent(CreateView):

    template_name = "event/addEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')
