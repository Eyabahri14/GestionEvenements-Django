from django.shortcuts import render, redirect
from .models import Event,participants
from django.views.generic import *
from .forms import EvenementForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from person.models import Person
# Create your views here.


def index(request, name):

    text = f"Hello {name}"
    return HttpResponse(text)



# def custom_login_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return view_func(request, *args, **kwargs)
#         else:
#             login_url = reverse_lazy('login')
#             return redirect(login_url)
#     return wrapper

@login_required
def list_event(request):

    list = Event.objects.filter(state=True).order_by('evt_date')

    Nbr = Event.objects.count()

    return render(request, 'event/list_event.html', {'events': list})

 

 
class ListEvents(LoginRequiredMixin ,ListView):

    model = Event
    template_name = "event/list_event.html"
    
    context_object_name = "events"  # par défaut object_list
    login_url = 'login'
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
            print(form.instance)
            form.instance.organisateur=Person.objects.get(cin=req.user.cin)
            # print(form.instance.organisateur)
            form.save()
            return redirect('Affiche')
    return render(req, 'event/addEvent.html', {'form': form})

def participer(req, event_id):
    user = req.user

    event = Event.objects.get(id=event_id)

    participant = participants.objects.create(
        person=user, evenement=event)
    participant.save()
    event.nbr_participant += 1
    event.save()

    return redirect('Affiche')


def cancel(req,event_id):
    user = req.user

    event = Event.objects.get(id=event_id)
    participant = participants.objects.get(person = user, evenement = event)
    participant.delete()
    event.nbr_participant-=1
    event.save()
    return redirect('Affiche')

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


def eventDetails(req, id):
    user = req.user
    event = Event.objects.get(id=id)
    if user:
        participant = participants.objects.filter(
            person=user, evenement=event)
        if participant:     
            button_disabled = True
        else:
            button_disabled = False
    return render(req, "event/details.html", {'e': event, "button": button_disabled})
