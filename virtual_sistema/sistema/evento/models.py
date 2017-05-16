from datetime import datetime
from django.db import models


class Evento(models.Model):
    nome = models.CharField("Nome do evento",max_length = 200)
    descricao = models.CharField("Descrição",max_length = 200)
    endereco = models.CharField("Endereço",max_length = 200)
    local = models.CharField("Local",max_length = 200)
    numeroVagas = models.IntegerField("Número de Vagas")
    numeroInscritos = models.IntegerField(default=0)
    dataInicio = models.DateField("Data de Início")
    dataFim = models.DateField("Data de Fim")


    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.descricao)


TIPO_PROGRAMACAO = (
    (1,'Mini-curso'),
    (2,'Palestra'),
    (3,'WorkShop'),
    (4,'Apresentação de Trabalho')
)
# Create your models here.
class Programacao(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 400)
    tipo = models.IntegerField(choices=TIPO_PROGRAMACAO, default=2)
    dataInicio = models.DateTimeField("Início",null=False)
    dataFim = models.DateTimeField("Fim",null=False)
    evento = models.ForeignKey(Evento)

    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.evento)
