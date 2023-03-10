
from .models import Event
from django.forms import *
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class EvenementForm(ModelForm):

    class Meta:
        model = Event
        fields = "__all__"

        exclude = ('participant', 'state', 'nbr_participant','organisateur')
        widgets = {'description': TextInput(
            attrs={'cols': 10, 'rows': 10, 'class': 'form-control'}
        ), 'evt_date': DateInput(), }
