from django import forms
from .models import *


class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = ['numeroInscritos']

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['dataInicio'].widget.attrs['class'] = 'datepicker'
        self.fields['dataFim'].widget.attrs['class'] = 'datepicker'

class ProgramacaoForm(forms.ModelForm):

    class Meta:
        model = Programacao
        exclude = ['evento']

    def __init__(self, *args, **kwargs):
        super(ProgramacaoForm, self).__init__(*args, **kwargs)
        self.fields['dataInicio'].widget.attrs['class'] = 'datepicker'
        self.fields['dataFim'].widget.attrs['class'] = 'datepicker'
