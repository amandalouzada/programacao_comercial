# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from const import *

# Create your models here.
class Mesa(models.Model):
    numero = models.IntegerField(max_digits =3)
    data = models.DateField(default=datetime.now)

    def __str__(self):
        return self.numero