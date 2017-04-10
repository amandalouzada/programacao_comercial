from django.db import models
from evento.models import *

# Create your models here.
class Horario(models.Model):
    dataInicio = models.DateField(default=datetime.now)
    dataFim = models.DateField(default=datetime.now)
    evento = models.ForeignKey(Evento, null=True)


    def __str__(self):
        return '{0} - {1}'.format(self.dataInicio, self.dataFim)
