from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from .models import Produto


# Create your views here.

class ListarProdutos(ListView):
    """
    View para listar os Produtos cadastrados
    """
    login_url = '/'
    model = Produto
    template_name = 'produto/listar_Produtos.html'
