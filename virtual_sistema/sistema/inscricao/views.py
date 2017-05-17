from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse


# Create your views here.
class Credenciamento(TemplateView):
    model = Inscricao
    template_name = 'inscricao/credenciamento.html'
    form_class = InscricaoForm

    def get_context_data(self, **kwargs):
        self.context = super(Credenciamento, self).get_context_data(**kwargs)
        self.context['object'] = Evento.objects.get(pk=self.kwargs['pk'])
        return self.context

    def post(self, request, *args, **kwargs):

        inscricao = Inscricao.objects.get(pk=request.POST.get("numero"))
        print(inscricao.evento.pk)
        print(self.kwargs['pk'])

        if str(inscricao.evento.pk) == self.kwargs['pk']:
            inscricao.credenciado = 1
            inscricao.save()
            messages.error(request, 'O numero de vagas deve ser maior do que o número de inscritos' )
            return JsonResponse({'msg':'Credenciamento Realizado'})
        else:
            print("nao entrou")
            return JsonResponse({'msg':'Inscrição não encontrada. Verifique se está no evento correto'})

        return JsonResponse({'msg':'ERRO'})


class EventoListCredenciado(LoginRequiredMixin, ListView):
    login_url = "/"
    model = Inscricao
    template_name = 'inscricao/list.html'

    def get_context_data(self, **kwargs):
        self.context = super(EventoListCredenciado, self).get_context_data(**kwargs)
        self.context['object'] = Evento.objects.get(pk=self.kwargs['pk'])
        return self.context

    def get_queryset(self):
        queryset = Inscricao.objects.filter(evento=self.kwargs['pk'], credenciado=1)
        return queryset
