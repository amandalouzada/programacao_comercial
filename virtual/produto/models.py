# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from const import *

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length = 200)
    tipo_produto = models.IntegerField(choices=TIPO_PRODUTO, default=1)
    preco = models.DecimalField(max_digits = 9, decimal_places=2)
    descricao = models.CharField(max_length = 200)
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return '{0} - {1}'.format(self.nome, self.descricao)