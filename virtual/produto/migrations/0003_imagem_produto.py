# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160803171240 on 2017-02-27 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20170227_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.Produto'),
        ),
    ]