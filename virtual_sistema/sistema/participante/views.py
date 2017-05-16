from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView, DetailView, TemplateView
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import ParticipanteMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
class UsuarioCreate(CreateView):
    model = User
    form_class= UsuarioForm
    template_name = 'participante/novo-usuario.html'
    success_url = reverse_lazy('novo-participante')


    def get_context_data(self, **kwargs):
        self.context = super(UsuarioCreate, self).get_context_data(**kwargs)
        self.context['form'] = UsuarioForm()
        return self.context

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
            messages.error(request, form.errors)
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


class ParticipanteUpdate(TemplateView):
    model = Participante
    form_participante = ParticipanteForm
    form_usuario = UsuarioForm
    template_name = 'participante/update.html'
    success_url = reverse_lazy('index')
    fail_url = reverse_lazy('update-participante')

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


class ParticipanteList(LoginRequiredMixin, ParticipanteMixin, ListView):
    login_url = "/"
    permission_required="auth.change_user"
    model = Participante
    template_name = 'participante/listar.html'


class ParticipanteDetalhe(LoginRequiredMixin, ParticipanteMixin, DetailView):
    login_url = "/"
    model = Participante
    template_name = 'participante/detalhe.html'
