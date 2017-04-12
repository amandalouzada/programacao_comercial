from django import forms
from .models import *


class ParticipanteForm(forms.ModelForm):

    class: Meta:
        model = Evento
        exclude = []
