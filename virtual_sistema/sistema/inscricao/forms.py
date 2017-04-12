from django import forms
from .models import *


class InscricaoForm(forms.ModelForm):

    class: Meta:
        model = Inscricao
        exclude = []
