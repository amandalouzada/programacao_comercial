from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, View, RedirectView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from inscricao.models import *
from inscricao.forms import *




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


class EventoInscricao(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        participante = Participante.objects.get(usuario = request.user)
        inscricao = Inscricao.create(evento= evento, participante = participante)
        inscricao.save()
        return redirect(reverse_lazy('listar-eventos'))
