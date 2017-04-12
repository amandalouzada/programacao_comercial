from datetime import datetime
from django.db import models


class Evento(models.Model):
    nome = models.CharField(max_length = 200)
    descricao = models.CharField("Descrição",max_length = 200)
    local = models.CharField("Local",max_length = 200)
    endereco = models.CharField("Endereço",max_length = 200)
    numeroVagas = models.IntegerField()
    dataInicio = models.DateField()
    dataFim = models.DateField()


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.descricao)
