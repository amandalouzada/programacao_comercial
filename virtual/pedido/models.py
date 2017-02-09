# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from mesa.models import *
from produto.models import *


from const import *

# Create your models here.
class Pedido(models.Model):
    data = models.DateField(default=datetime.now)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return '{0} - {1}'.format(self.preco, self.nome)