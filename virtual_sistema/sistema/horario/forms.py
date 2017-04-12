from django import forms
from .models import *


class HorarioForm(forms.ModelForm):

    class: Meta:
        model = Horario
        exclude = []
