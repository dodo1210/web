# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20170607_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coment_publi',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='coment_publicacao_grupo_de_estudo',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='forum_duvida',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='publicacao_grupo_de_estudo',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='resp_forum_duvida',
            name='perfil',
        ),
    ]
