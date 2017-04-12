from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .forms import *


class EventoCreate(CreateView):
    model = Evento
    form_class= EventoForm
    template_name = 'evento/create.html'
