from django.shortcuts import render

from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



class Autenticacao(View):
    def get(self,request):
        if request.user.is_authenticated():
            return redirect(reverse_lazy('listar-produtos'))
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
            return redirect(reverse_lazy('listar-produtos'))
        else:
            resposta['mensagem'] = 'Usuário ou senha incorreto'
            resposta['login'] = usuario

        return render(request, 'autenticacao/login.html', resposta)


class Logout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('/')
