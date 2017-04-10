from django import forms
from .models import *


class FormularioPedido(forms.ModelForm):
    """
    Formulario para o model Pedido
    """
    class Meta:
        model = Pedido
        exclude = ['data']
    def __init__(self, *args, **kwargs):
        super(FormularioPedido, self).__init__(*args, **kwargs)
