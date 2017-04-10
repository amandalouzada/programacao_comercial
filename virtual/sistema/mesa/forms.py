from django import forms
from .models import *


class FormularioMesa(forms.ModelForm):
    """
    Formulario para o model Mesa
    """
    class Meta:
        model = Mesa
        exclude = ['data']
    def __init__(self, *args, **kwargs):
        super(FormularioMesa, self).__init__(*args, **kwargs)
