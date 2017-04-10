from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Mesa
from .forms import *

from django.http import Http404
from django.core import serializers

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ListarMesas(LoginRequiredMixin, ListView):
    """
    View para listar os Produtos cadastrados
    """
    login_url = "/"
    model = Mesa
    template_name = 'mesa/listar_mesas.html'
    form_class = FormularioMesa

    def get_queryset(self):
        queryset = Mesa.objects.order_by('numero')

        return queryset


class NovaMesa(LoginRequiredMixin, CreateView):
    """
    View para criação de novas Mesas
    """
    login_url = "/"
    model = Mesa
    form_class = FormularioMesa
    template_name = 'mesa/nova_mesa.html'
    success_url = reverse_lazy('listar-mesas')

    def get_context_data(self, **kwargs):
        self.context = super(NovaMesa, self).get_context_data(**kwargs)
        return self.context



def novasMesas(LoginRequiredMixin, request, qtd_mesa):

    login_url = "/"
    x = 0
    for x in range(int(qtd_mesa)):
        mesa = Mesa()
        mesa.save()

    return redirect(reverse_lazy('listar-mesas'))


class UpdateMesa(LoginRequiredMixin, UpdateView):
    """
    View para criação de novos Produtos
    """
    login_url = "/"
    model = Mesa
    form_class = FormularioMesa
    template_name = 'mesa/update_mesa.html'
    success_url = reverse_lazy('listar-mesas')

    def get_context_data(self, **kwargs):
        self.context = super(UpdateMesa, self).get_context_data(**kwargs)
        return self.context
