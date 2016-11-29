from django import forms
from usuario.models import *

class FormularioUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        exclude = []
