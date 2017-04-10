# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from .const import *

# Create your models here.
class Mesa(models.Model):
    numero = models.AutoField(primary_key=True)
    data = models.DateField(default=datetime.now)
    status = models.IntegerField(choices=STATUS_MESA, default=0)

    def __str__(self):
        return self.numero
