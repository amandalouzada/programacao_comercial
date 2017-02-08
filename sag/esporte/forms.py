from django import forms
from .models import *

class FormularioAtleta(forms.ModelForm):
    dataNascimento = forms.DateField(label='Data de Nascimento')
    cpf = forms.DateField(label='CPF')


    class Meta:
        model = Atleta
        exclude = []
    def __init__(self,*args,**kwargs):
        super(FormularioAtleta, self).__init__(*args,**kwargs)
        self.fields['nome'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['matricula'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['cpf'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['dataNascimento'].widget.attrs['class'] = 'datepicker blue-grey lighten-5'
        self.fields['email'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['curso'].widget.attrs['class'] = 'blue-grey lighten-5'


class FormularioTecnico(forms.ModelForm):
    crefi = forms.DateField(label='CREFI')

    class Meta:
        model = Tecnico
        exclude = []
    def __init__(self,*args,**kwargs):
        super(FormularioTecnico, self).__init__(*args,**kwargs)
        self.fields['nome'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['cpf'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['email'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['crefi'].widget.attrs['class'] = 'blue-grey lighten-5'



class FormularioModalidade(forms.ModelForm):
    qtdMaxAtletas = forms.DateField(label='Quantidade Maxima de Atletas')

    class Meta:
        model = Modalidade
        exclude = []
    def __init__(self,*args,**kwargs):
        super(FormularioModalidade, self).__init__(*args,**kwargs)
        self.fields['nome'].widget.attrs['class'] = 'blue-grey lighten-5'
        self.fields['qtdMaxAtletas'].widget.attrs['class'] = 'blue-grey lighten-5'
