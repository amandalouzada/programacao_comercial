from django import forms
from .models import *


class FormularioProduto(forms.ModelForm):
    """
    Formulario para o model Produto
    """
    class Meta:
        model = Produto
        exclude = ['data']
    def __init__(self, *args, **kwargs):
        super(FormularioProduto, self).__init__(*args, **kwargs)
        #NOME
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['title'] = 'Somente letras'


class FormularioImagem(forms.ModelForm):

    class Meta:
        model = Imagem
        fields = ['nome','produto', 'imageFile']
