# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 15:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directiva',
            old_name='FechaDeFinalización',
            new_name='FechaDeFinalizacion',
        ),
    ]