from django import forms
from .models import *
from django.contrib.auth.models import User


class ParticipanteForm(forms.ModelForm):

    class Meta:
        model = Participante
        exclude = ['usuario','status']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['first_name','last_name','email','username']
        fields = ['first_name','last_name','email','username','password']
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'username':'Nome do usuário'
        }
        widgets = {
            'password': forms.PasswordInput
        }
    # def __init__(self, *args, **kwargs):
    #     self.fields['password'].widget.attrs['type'] = 'password'
