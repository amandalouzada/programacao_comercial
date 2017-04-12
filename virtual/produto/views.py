from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Produto
from .forms import *


from django.core import serializers

from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect


# Create your views here.

class ListarProdutos(ListView):
    """
    View para listar os Produtos cadastrados
    """
    model = Produto
    template_name = 'produto/listar_Produtos.html'



class ListarProdutosTipo(ListView):
    """
    View para listar os Produtos cadastrados
    """
    model = Produto
    template_name = 'produto/listar_Produtos.html'

    def get_queryset(self):
        queryset = Produto.objects.filter(tipo_produto=self.kwargs['tipo_produto'])
        return queryset

class NovoProduto(CreateView):
    """
    View para criação de novos Produtos
    """
    model = Produto
    form_class = FormularioProduto
    template_name = 'produto/novo_produto.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        self.context = super(NovoProduto, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Produto'
        return self.context


class UpdateProduto(UpdateView):
    """
    View para criação de novos Produtos
    """
    model = Produto
    form_class = FormularioProduto
    template_name = 'produto/detalhe_produto.html'
    success_url = reverse_lazy('update-produto')

    def get_context_data(self, **kwargs):
        self.context = super(UpdateProduto, self).get_context_data(**kwargs)
        self.context['nome'] = 'Atualizar produto'
        return self.context





class NovoImagem(CreateView):
    model = Imagem
    form_class = FormularioImagem
    template_name = 'produto/novo_imagem.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        self.context = super(NovoImagem, self).get_context_data(**kwargs)
        self.context['nome'] = 'Novo Imagem'
        return self.context
