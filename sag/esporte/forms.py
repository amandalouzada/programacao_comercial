from django import forms
from .models import *

class FormularioAtleta(forms.ModelForm):

    class Meta:
        model = Atleta
        exclude = []
