from django.shortcuts import render, redirect
from .models import Event
from django.views.generic import *
from .forms import EvenementForm
from django.urls import reverse_lazy

from django.http import HttpResponse
# Create your views here.


def index(request, name):

    text = f"Hello {name}"
    return HttpResponse(text)


def list_event(request):

    list = Event.objects.filter(state=True).order_by('evt_date')

    Nbr = Event.objects.count()

    return render(request, 'event/list_event.html', {'events': list})


class ListEvents(ListView):

    model = Event
    template_name = "event/list_event.html"
    context_object_name = "events"  # par défaut object_list

    def get_queryset(self):
        eventsTrue = Event.objects.filter(state=True).order_by('evt_date')
        return eventsTrue


class AddEvent(CreateView):

    template_name = "event/addEvent.html"
    model = Event
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')


def AddEv(req):
    form = EvenementForm()
    if req.method == 'POST':
        form = EvenementForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('Affiche')
    return render(req, 'event/addEvent.html', {'form': form})


class ModifierEvenement(UpdateView):
    model = Event
    template_name = "event/updateEvent.html"
    form_class = EvenementForm
    success_url = reverse_lazy('Affiche')


class DeleteEvent(DeleteView):
    model = Event
    template_name = "event/deleteEvent.html"
    success_url = reverse_lazy('Affiche')


class DetailsEvent(DetailView):
    model = Event
    template_name = "event/details.html"
    context_object_name = "event"  # par défaut object_list


def detailsss(req, pk):

    event = Event.objects.get(id=pk)

    return render(req, "event/details.html", {'e': event})
