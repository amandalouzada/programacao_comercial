from django import forms
from .models import *


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = []
