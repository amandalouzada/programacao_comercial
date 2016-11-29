from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    matricula = models.CharField(max_length=12)
    senha = models.CharField(max_length=20)
    # permissao = models.SmallIntegerField(choices=[(1, 'MONITOR'), (2, 'ALUNO'),(3, 'PROFESSOR')])

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.matricula, self.senha)

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    semestre = models.PositiveIntegerField()

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.ano, self.semestre)

class Monitor(Usuario):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Professor(Usuario):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Duvida(models.Model):
    nome = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=700)
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True, blank=True)
