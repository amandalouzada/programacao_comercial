from django.db import models
from evento.models import *
from participante.models import *


# Create your models here.

class Inscricao(models.Model):
    class Meta:
        unique_together = (('evento','participante'))


    data = models.DateField(default=datetime.now)
    ativa = models.IntegerField(default=1)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, null=False)

    @classmethod
    def create(cls, evento, participante):
        inscricao = cls(evento=evento, participante=participante)
        return inscricao

    def __str__(self):
        return '{0} - {1}'.format(self.data, self.participante)
