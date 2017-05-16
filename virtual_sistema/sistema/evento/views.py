from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, View, RedirectView, TemplateView
from .forms import *
from participante.mixins import *
from django.contrib.auth.mixins import LoginRequiredMixin
from inscricao.models import *
from inscricao.forms import *
from django.contrib import messages




class EventoCreate(LoginRequiredMixin, ParticipanteMixin, CreateView):
    login_url = "/"
    model = Evento
    form_class= EventoForm
    template_name = 'evento/novo.html'
    success_url = reverse_lazy('listar-eventos')
    fail_url = reverse_lazy('novo-evento')

    def post(self, request, *args, **kwargs):
        print(request.POST)
        # form = EventoForm(request.POST)
        # for horario in request.POST.getlist("horario"):
        #     print(horario)
        #
        # if form.is_valid():
        #     evento = form.save(commit=False)
        #     if (evento.dataInicio <= evento.dataFim):
        #         evento.save()
        #         return redirect(self.success_url)
        #     else:
        #         messages.error(request, 'Data de início deve ser menor que a data de fim')
        #         return redirect(self.fail_url)
        # else:
        #     messages.error(request, form.errors)
        #     return redirect(self.fail_url)
        return redirect(self.fail_url)



class EventoList(LoginRequiredMixin, ListView):
    login_url = "/"
    model = Evento
    template_name = 'evento/listar.html'


class EventoDetalhe( TemplateView ):
    template_name = 'evento/detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(EventoDetalhe, self).get_context_data(**kwargs)
        context['object'] = Evento.objects.get(pk=self.kwargs['pk'])
        context['inscritos'] = Inscricao.objects.filter(evento=self.kwargs['pk'])
        try:
            status = Inscricao.objects.get(evento=self.kwargs['pk'], participante=Participante.objects.get(usuario=self.request.user.pk))
            if status :
                context['status']= True
            else:
                context['status']= False
        except Exception as e:
            return context
        return context

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            evento = Evento.objects.get(pk=kwargs['pk'])
            try:
                participante = Participante.objects.get(usuario = request.user)
            except Exception as e:
                return redirect(reverse_lazy('novo-participante'))
            try:
                inscricao = Inscricao.create(evento= evento, participante = participante)
                inscricao.save()
            except Exception as e:
                messages.error(request, 'Usuário já inscrito no evento')

                return redirect(reverse_lazy('detalhe-evento', kwargs={'pk':kwargs['pk']}))

            return redirect(reverse_lazy('listar-eventos'))

        else:
            return redirect(reverse_lazy('novo-usuario'))




class EventoListInscricao(LoginRequiredMixin, ParticipanteMixin, ListView):
    login_url = "/"
    model = Inscricao
    template_name = 'evento/inscricoes.html'

    def get_context_data(self, **kwargs):
        self.context = super(EventoListInscricao, self).get_context_data(**kwargs)
        return self.context

    def get_queryset(self):
        queryset = Inscricao.objects.filter(evento=self.kwargs['pk'])
        return queryset


class ProgramacaoCreate(LoginRequiredMixin, ParticipanteMixin, TemplateView):
    login_url="/"
    model = Programacao
    form_class= ProgramacaoForm
    template_name = 'evento/programacao.html'

    def get_context_data(self, **kwargs):
        context = super(ProgramacaoCreate, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        context['id'] = kwargs['pk']
        return context

    def post(self, request, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        form = ProgramacaoForm(request.POST)
        if form.is_valid():
            programacao = form.save(commit=False)
            programacao.evento = evento
        try:
            programacao.save()
        except Exception as e:
            return redirect(reverse_lazy('listar-eventos'))
