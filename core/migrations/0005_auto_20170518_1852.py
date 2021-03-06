# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 18:52
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_forum_duvida_resp_forum_duvida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment_ublicacao_Grupo_de_Estudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.TextField(blank=True, verbose_name='comentario_grup')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_de_Estudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem_logo', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_profileimage)),
                ('area', models.ManyToManyField(to='core.Obt_Estudo')),
                ('participantes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao_Grupo_de_Estudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField(blank=True, verbose_name='texto_grup')),
                ('anexo', models.FileField(blank=True, upload_to=core.models.user_directory_path)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('area', models.ManyToManyField(to='core.Obt_Estudo')),
                ('grupo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Grupo_de_Estudo')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seguidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amigos', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='forum_duvida',
            name='texto',
            field=models.TextField(blank=True, verbose_name='texto_forum'),
        ),
        migrations.AddField(
            model_name='coment_ublicacao_grupo_de_estudo',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Grupo_de_Estudo'),
        ),
        migrations.AddField(
            model_name='coment_ublicacao_grupo_de_estudo',
            name='publi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Publicacao_Grupo_de_Estudo'),
        ),
        migrations.AddField(
            model_name='coment_ublicacao_grupo_de_estudo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
