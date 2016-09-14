from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from usuario.models import *

# Create your views here.
def index(request):
    return HttpResponse("Olá Monitor.")

class UsuarioIndex(ListView):
    model = Usuario
    template_name = 'usuario/index.html'

def login(request):
	model = Usuario
	return render(request, 'usuario/login.html')