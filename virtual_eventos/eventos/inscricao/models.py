from django.db import models
from evento.models import *
from presenca.models import *

# Create your models here.

class Inscricao(models.Model):
    data = models.DateField(default=datetime.now)
    ativa = modelsIntegerField(default=1)
    homologada = modelsIntegerField(default=0)
    codigo = modelsIntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    presencas = models.ManyToManyField(Presencas)


    def __str__(self):
        return '{0} - {1}'.format(self.data, self.codigo)
