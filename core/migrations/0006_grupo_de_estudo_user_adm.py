# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170518_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo_de_estudo',
            name='user_adm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Perfil'),
        ),
    ]