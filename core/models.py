# -*- coding: utf 8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User
import PIL
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


def user_directory_profileimage(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/profile/{1}'.format(instance.user.username, filename)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/uploads/{1}'.format(instance.user.username, filename)


class Obt_Estudo(models.Model):
	nome = models.CharField(max_length=100, verbose_name='Objetos')

	def __str__(self):
		return self.nome

class Perfil(models.Model):
	user = models.OneToOneField(User, related_name='Perfil')
	bio = models.TextField(verbose_name='Bio', blank=True)
	imagem_perfil = models.ImageField(verbose_name='Imagem',blank=True, null=True, upload_to=user_directory_profileimage)
	data_cadastro = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)
	data_altera = models.DateTimeField(verbose_name='Data_Alteracao',default=timezone.now)

	def __str__(self):
		return self.user.username

class Publicacao(models.Model):
	user   = models.ForeignKey(User, default=1)
	titulo = models.CharField(verbose_name='Titulo',max_length=100)
	texto  = models.TextField(verbose_name='Texto', blank=True)
	anexo  = models.FileField(verbose_name='Anexo',blank=True, upload_to=user_directory_path)
	area   = models.ManyToManyField(Obt_Estudo)
	data   = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)
	
	def __str__(self):
		return self.user.username + ' publicou ' + self.titulo

class Coment_Publi(models.Model):
	user = models.ForeignKey(User, default=1)
	publi = models.ForeignKey(Publicacao)
	coment = models.TextField(verbose_name='Comentario', blank=True)
	data = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)
	
	def __str__(self):
		return self.user.username + ' comentou em ' + self.publi.titulo

class Forum_Duvida(models.Model):
	user   = models.ForeignKey(User, default=1)
	area   = models.ManyToManyField(Obt_Estudo)
	data   = models.DateTimeField(default=timezone.now)
	texto  = models.TextField(verbose_name='Texto', blank=True)

	def __str__(self):
		return self.user.username + ' publicou um forum!'


class Resp_Forum_Duvida(models.Model):
	user = models.ForeignKey(User, default=1)
	forum = models.ForeignKey(Forum_Duvida, default=1)
	resp = models.TextField(verbose_name='Resposta', blank=True)
	data = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)
	melhor_resposta = models.BooleanField(verbose_name='Melhor_Resposta',default=False)

	def __str__(self):
		return self.user.username + ' publicou uma resposta para ' + self.forum.texto

class Grupo_de_Estudo(models.Model):
	user_adm = models.ForeignKey(Perfil, default=1)
	area   = models.ManyToManyField(Obt_Estudo)
	titulo = models.CharField(max_length=100)
	imagem_logo = models.ImageField(blank=True, null=True, upload_to=user_directory_profileimage)
	participantes  = models.ManyToManyField(User)

	def __str__(self):
		return self.titulo

class Publicacao_Grupo_de_Estudo(models.Model):
	user   = models.ForeignKey(User, default=1)
	grupo  = models.ForeignKey(Grupo_de_Estudo, default=1)
	titulo = models.CharField(max_length=100)
	texto  = models.TextField(verbose_name='Texto', blank=True)
	anexo  = models.FileField(verbose_name='Anexo',blank=True, upload_to=user_directory_path)
	area   = models.ManyToManyField(Obt_Estudo)
	data   = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)
	
	def __str__(self):
		return self.user.username + ' publicou ' + self.titulo + 'em ' + self.grupo.titulo

class Coment_Publicacao_Grupo_de_Estudo(models.Model):
	user = models.ForeignKey(User, default=1)
	grupo  = models.ForeignKey(Grupo_de_Estudo, default=1)
	publi = models.ForeignKey(Publicacao_Grupo_de_Estudo, default=1)
	coment = models.TextField(verbose_name='Comentario', blank=True)
	data = models.DateTimeField(verbose_name='Data_Cadastro',default=timezone.now)

	def __str__(self):
		return self.user.username + ' publicou ' + self.publi.titulo
		
class Seguidor(models.Model):
	user  =  models.OneToOneField(User, related_name='amigos')
	amigos = models.ForeignKey(User, default=1)