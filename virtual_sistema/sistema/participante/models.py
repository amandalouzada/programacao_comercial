from django.db import models

from django.contrib.auth.models import User


class Participante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCracha = models.CharField(max_length = 200)
    instituicao = models.CharField("Instituição",max_length = 200)
    celular = models.CharField("Celular",max_length = 15)
    endereco = models.CharField("Endereço",max_length = 200)
    municipio = models.CharField("Município",max_length = 20)
    uf = models.DateField("UF",max_length = 2)
    status = models.IntegerField()
    codigoConfirmacao =models.CharField("Codigo de confirmação",max_length = 200)


    def __str__(self):
        return '{0} - {1}'.format(self.nomeCracha, self.instituicao)
