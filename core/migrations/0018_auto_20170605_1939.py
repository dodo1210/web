# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-05 19:39
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170605_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo_de_estudo',
            name='imagem_logo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path, verbose_name='Logo'),
        ),
    ]
