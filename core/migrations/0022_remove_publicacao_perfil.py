# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20170607_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacao',
            name='perfil',
        ),
    ]