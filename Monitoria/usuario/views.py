from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from usuario.models import *
from usuario.forms import *

# Create your views here.
class UsuarioIndex(ListView):
    model = Usuario
    template_name = 'usuario/index.html'

def login(request):
	return render(request, 'usuario/login.html')


class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario/listar.html'


class UsuarioNew(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/novo.html'
    success_url = reverse_lazy('listar-usuario')

class UsuarioEdit(UpdateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/editar.html'
    success_url = reverse_lazy('listar-usuario')
