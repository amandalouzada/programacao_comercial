# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160803171240 on 2017-02-27 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='url',
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imageFile',
            field=models.ImageField(upload_to='produto'),
        ),
    ]
