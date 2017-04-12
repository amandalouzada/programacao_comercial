# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from const import *

# Create your models here.
class Ingrediente(models.Model):
    nome = models.CharField(max_length = 200)
    qtd = models.IntegerField()
    tipo_medida = models.IntegerField(choices=TIPO_MEDIDA, default=3)
    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.qtd)