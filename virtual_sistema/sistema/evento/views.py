from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin



class EventoCreate(LoginRequiredMixin, CreateView):
    login_url = "/"
    model = Evento
    form_class= EventoForm
    template_name = 'evento/novo.html'
    success_url = reverse_lazy('listar-eventos')


class EventoList(LoginRequiredMixin, ListView):
    login_url = "/"
    model = Evento
    template_name = 'evento/listar.html'


class EventoDetalhe(LoginRequiredMixin, DetailView):
    login_url = "/"
    model = Evento
    template_name = 'evento/detalhe.html'
