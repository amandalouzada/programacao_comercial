from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.core.validators import *
from django.utils import timezone

class Atleta(models.Model):
    matricula = models.PositiveIntegerField()
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length = 14, validators = [
                                    RegexValidator(regex=r'^\d\d\d\.\d\d\d\.\d\d\d-\d\d$',
                                        message = ("Verifique o CPF"),
                                        code = 'cpf_invalido')
                                    ]
                            )
    curso = models.CharField(max_length = 100)
    dataNascimento = models.DateField(auto_now = False)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.matricula, self.curso, self.dataNascimento)


class Tecnico(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length = 14, validators = [
                                    RegexValidator(regex=r'^\d\d\d\.\d\d\d\.\d\d\d-\d\d$',
                                        message = ("Verifique o CPF"),
                                        code = 'cpf_invalido')
                                    ]
                            )
    crefi = email = models.CharField(max_length=30, blank = True)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.cpf, self.crefi)


class Modalidade(models.Model):
    nome = models.CharField(max_length = 50)
    qtdMaxAtletas = models.PositiveIntegerField(blank = True)

    def __str__(self):
        return self.nome


class Local(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.endereco)

class Material(models.Model):
    nome = models.CharField(max_length = 50)
    quantidade = models.PositiveIntegerField()
    patrimonio = models.PositiveIntegerField( blank = True)
    descricao = models.CharField(max_length=200, blank = True)
    modalidades = models.ManyToManyField(Modalidade)


    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length = 50)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    qtdAtletas = models.PositiveIntegerField()
    descricao = models.CharField(max_length=200, blank = True)
    atletas = models.ManyToManyField(Atleta)


    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.descricao)


class Evento(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length=200, blank = True)
    dataInicio = models.DateField(auto_now = False , blank = True)
    dataFim = models.DateField(auto_now = False, blank = True)
    equipes = models.ManyToManyField(Atleta)
    tipo = models.SmallIntegerField(choices=[(1, 'NACIONAL-UNIVERSTARIO'), (2, 'ESTADUAL-UNIVERSTARIO'),(3, 'REGIONAL-UNIVERSTARIO'), (4, 'NACIONAL'), (5, 'ESTADUAL'), (6, 'REGIONAL'), (7, 'OUTRO')])



    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.descricao)
