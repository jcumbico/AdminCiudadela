# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-17 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181017_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='Manzana',
        ),
    ]
