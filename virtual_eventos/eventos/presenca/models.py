from django.db import models
from horario.models import *
from inscricao.models import *


# Create your models here.
# Create your models here.
class Presenca(models.Model):
    data = models.DateField(default=datetime.now)
    status = models.IntegerField(max_digits=1)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    inscricao = models.ForeignKey(Inscricao, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.data, self.status)
