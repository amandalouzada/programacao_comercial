from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    matricula = models.CharField(max_length=12)
    senha = models.CharField(max_length=20)
    permissao = models.SmallIntegerField(choices=[(1, 'ADMINISTRADOR'), (2, 'USUARIO')])

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.matricula, self.senha)
