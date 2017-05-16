# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('tipo', models.IntegerField(choices=[(1, 'Mini-curso'), (2, 'Palestra'), (3, 'WorkShop'), (4, 'Apresentação de Trabalho')], default=2)),
                ('nome', models.CharField(max_length=100)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evento.Evento')),
            ],
        ),
    ]