from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.


# def atleta(request):
#     print ("Amanda")
#     model = Atleta
#     return render(request, 'esporte/atleta.html', {})
#
#
# def listar(request):
#     print ("Louzada")
#     model = Atleta
#
#     queryset = Atleta.objects.filter()
#     print (queryset)
#
#     return render(request, 'esporte/atleta.html', {queryset})
#


class ListarAtleta(ListView):
    model = Atleta
    template_name = 'esporte/atleta/atleta.html'


    def get_context_data(self, **kwargs):
        self.context = super(ListarAtleta, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Atleta'
        self.context['form'] = FormularioAtleta()
        return self.context

    def get_queryset(self):
        queryset = Atleta.objects.filter()
        return queryset

  # Create your views here.

class NovoAtleta(CreateView):
    model = Atleta
    form_class = FormularioAtleta
    template_name = 'esporte/atleta/atleta.html'
    success_url = reverse_lazy('listar-atletas')


class DeletarAtleta(DeleteView):
    model = Atleta
    form_class = FormularioAtleta
    success_url = reverse_lazy('listar-atletas')
    def get_context_data(self, **kwargs):
        self.context = super(DeletarAtleta, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Deletar tecnico'
        return self.context


class ListarTecnico(ListView):
    model = Tecnico
    template_name = 'esporte/tecnico/tecnico.html'


    def get_context_data(self, **kwargs):
        self.context = super(ListarTecnico, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Tecnico'
        self.context['form'] = FormularioTecnico()
        return self.context

    def get_queryset(self):
        queryset = Tecnico.objects.filter()
        return queryset

  # Create your views here.

class NovoTecnico(CreateView):
    model = Tecnico
    form_class = FormularioTecnico
    template_name = 'esporte/tecnico/tecnico.html'
    success_url = reverse_lazy('listar-tecnicos')


class DeletarTecnico(DeleteView):
    model = Tecnico
    form_class = FormularioTecnico
    success_url = reverse_lazy('listar-tecnicos')
    def get_context_data(self, **kwargs):
        self.context = super(DeletarTecnico, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Deletar tecnico'
        return self.context


class ListarModalidade(ListView):
    model = Modalidade
    template_name = 'esporte/modalidade/modalidade.html'


    def get_context_data(self, **kwargs):
        self.context = super(ListarModalidade, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Modalidade'
        self.context['form'] = FormularioModalidade()
        return self.context

    def get_queryset(self):
        queryset = Modalidade.objects.filter()
        return queryset

  # Create your views here.

class NovoModalidade(CreateView):
    model = Modalidade
    form_class = FormularioModalidade
    template_name = 'esporte/modalidade/modalidade.html'
    success_url = reverse_lazy('listar-modalidades')


class DeletarModalidade(DeleteView):
    model = Modalidade
    form_class = FormularioModalidade
    success_url = reverse_lazy('listar-modalidades')
    def get_context_data(self, **kwargs):
        self.context = super(DeletarModalidade, self).get_context_data(**kwargs)
        self.context['titulo'] = 'Deletar modalidade'
        return self.context
