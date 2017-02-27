# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from .const import *

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length = 200)
    tipo_produto = models.IntegerField(choices=TIPO_PRODUTO, default=1)
    preco = models.DecimalField("Preço", max_digits = 9, decimal_places=2)
    descricao = models.CharField("Descrição",max_length = 200)
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return '{0} - {1}'.format(self.get_tipo_produto_display(),self.nome, self.descricao)


class Imagem(models.Model):
    nome = models.CharField(max_length=150, blank=True)
    imageFile = models.ImageField(upload_to='produto')
    produto = models.ForeignKey(Produto, null=True, related_name='produtos')

    def get_absolute_url(self):
        return reverse('resource_detail', kwargs={'pk': self.id})
