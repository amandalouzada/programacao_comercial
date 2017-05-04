from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, View, RedirectView, TemplateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from inscricao.models import *
from inscricao.forms import *
from django.contrib import messages




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


class EventoDetalhe(LoginRequiredMixin, TemplateView):
    login_url = "/"
    template_name = 'evento/detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(EventoDetalhe, self).get_context_data(**kwargs)
        context['object'] = Evento.objects.get(pk=self.kwargs['pk'])
        return context

    def post(self, request, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        participante = Participante.objects.get(usuario = request.user)
        try:
            inscricao = Inscricao.create(evento= evento, participante = participante)
            inscricao.save()
        except Exception as e:
            messages.error(request, 'Usuário já inscrito no evento')

            return redirect(reverse_lazy('detalhe-evento', kwargs={'pk':kwargs['pk']}))

        return redirect(reverse_lazy('listar-eventos'))



class EventoListInscricao(LoginRequiredMixin, ListView):
    login_url = "/"
    model = Inscricao
    template_name = 'evento/inscricoes.html'

    def get_context_data(self, **kwargs):
        self.context = super(EventoListInscricao, self).get_context_data(**kwargs)
        return self.context

    def get_queryset(self):
        queryset = Inscricao.objects.filter(evento=self.kwargs['pk'])
        return queryset
