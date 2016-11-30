from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
class AtletasList(ListView):
  model = Atleta
  template_name = 'esporte/atleta_listar.html'
