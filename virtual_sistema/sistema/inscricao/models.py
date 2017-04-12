from django.db import models
from evento.models import *
from participante.models import *


# Create your models here.

class Inscricao(models.Model):
    data = models.DateField(default=datetime.now)
    ativa = models.IntegerField(default=1)
    homologada = models.IntegerField(default=0)
    codigo = models.IntegerField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, null=False)



    def __str__(self):
        return '{0} - {1}'.format(self.data, self.codigo)
