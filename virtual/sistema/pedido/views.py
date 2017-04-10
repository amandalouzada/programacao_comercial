# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import *
from .forms import *


class ListarPedidos(ListView):
    """
    View para listar os Pedidos cadastrados
    """
    model = Pedido
    template_name = 'pedido/listar_pedidos.html'



class NovoPedido(CreateView):
    """
    View para criação de novos Pedidos
    """
    model = Pedido
    form_class = FormularioPedido
    template_name = 'pedido/novo_pedido.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        self.context = super(NovoPedido, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Pedido'
        return self.context


class UpdatePedido(UpdateView):
    """
    View para criação de novos Pedidos
    """
    model = Pedido
    form_class = FormularioPedido
    template_name = 'pedido/detalhe_pedido.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        self.context = super(UpdatePedido, self).get_context_data(**kwargs)
        self.context['nome'] = 'Atualizar pedido'
        return self.context


class DeletarPedido(DeleteView):

    model = Pedido
    form_class = FormularioPedido
    success_url = reverse_lazy('listar-pedidos')
    template_name = 'pedido/deletar_pedido.html'


    def get_context_data(self, **kwargs):
        self.context = super(DeletarPedido, self).get_context_data(**kwargs)
        self.context['nome'] = 'Deletar pedido'
        return self.context
