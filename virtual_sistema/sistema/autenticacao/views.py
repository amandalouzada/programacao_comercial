from django.shortcuts import render

from django.views.generic import View, ListView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from evento.models import *



class Autenticacao(View):
    def get(self,request):
        if request.user.is_authenticated():
            return redirect(reverse_lazy('index'))
        else:
            return render(request,'autenticacao/login.html', {})


    def post(self,request):
        resposta={
            'sucesso': False,
            'mensagem': '',
            'login':'',
        }
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect(reverse_lazy('listar-eventos'))
        else:
            resposta['mensagem'] = 'Usuário ou senha incorreto'
            resposta['login'] = usuario

        return render(request, 'autenticacao/login.html', resposta)


class Logout(LoginRequiredMixin,View):
    login_url = "/"
    def get(self,request):
        logout(request)
        return redirect('/')


class Index(ListView):
    model = Evento
    template_name = 'index.html'
