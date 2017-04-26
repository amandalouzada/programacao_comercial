from datetime import datetime
from django.db import models


class Evento(models.Model):
    nome = models.CharField("Nome do evento",max_length = 200)
    descricao = models.CharField("Descrição",max_length = 200)
    local = models.CharField("Local",max_length = 200)
    endereco = models.CharField("Endereço",max_length = 200)
    numeroVagas = models.IntegerField("Número de Vagas")
    dataInicio = models.DateField("Data de Início")
    dataFim = models.DateField("Data de Fim")


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.descricao)
