# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20170610_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacao',
            name='perfil',
        ),
    ]
