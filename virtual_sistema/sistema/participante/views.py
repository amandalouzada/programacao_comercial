from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class UsuarioCreate(CreateView):
    model = User
    form_class= UsuarioForm
    template_name = 'participante/novo-usuario.html'
    success_url = reverse_lazy('novo-participante')

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print("formulario valido")
            post = form.save(commit=False)
            user = User.objects.create_user(post.username, post.email, post.password)
            user.last_name = post.last_name
            user.first_name = post.first_name
            user.save()
            if user:
                print("autenticado")
                login(request, user)
            else:
                print("nao autenticado")
                return redirect(reverse_lazy('novo-usuario'))
        else:
            print("invalidos")
            return redirect(reverse_lazy('novo-usuario'))

        return redirect(reverse_lazy('novo-participante'))



class ParticipanteCreate(CreateView):
    model = Participante
    form_class= ParticipanteForm
    template_name = 'participante/novo.html'
    success_url = reverse_lazy('index')
    fail_url = reverse_lazy('novo-participante')

    def post(self, request, *args, **kwargs):
        form = ParticipanteForm(request.POST)

        participante = form.save(commit=False)
        participante.usuario = request.user
        participante.status = 1
        participante.save()

        if participante:
            return redirect(self.success_url)
        else:
            return redirect(self.fail_url)


class ParticipanteList(LoginRequiredMixin, ListView):
    login_url = "/"
    model = Participante
    template_name = 'participante/listar.html'


class ParticipanteDetalhe(LoginRequiredMixin, DetailView):
    login_url = "/"
    model = Participante
    template_name = 'participante/detalhe.html'
