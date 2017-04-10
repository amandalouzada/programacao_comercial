# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from inscricao.models import *

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.CharField("Descrição",max_length = 200)
    local = models.CharField("Local",max_length = 200)
    endereco = models.CharField("Endereço",max_length = 200)
    numeroVagas = modelsIntegerField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    horarios = models.ManyToManyField(Horario)
    inscricoes = models.OneToManyField(Inscricao)


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.descricao)
from presenca.models import *
