# -*- coding: utf 8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Obt_Estudo,Perfil,Publicacao,Coment_Publi,Forum_Duvida,Resp_Forum_Duvida,Grupo_de_Estudo,Publicacao_Grupo_de_Estudo,Coment_Publicacao_Grupo_de_Estudo,Seguidor,EditUser

class RegisterForm(UserCreationForm):

	email = forms.EmailField(label = 'E-mail')
	first_name = forms.CharField(label = 'Primeiro Nome')
	last_name = forms.CharField(label = 'Sobrenome')

	def save(self,  commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = Perfil
		fields = ['imagem_perfil', 'bio']


class CadAreaForm(forms.ModelForm):
	
	class Meta:
		model = Obt_Estudo
		fields = ['nome']

class CadGrupForm(forms.ModelForm):

	class Meta:
		model = Grupo_de_Estudo
		fields = ['titulo','desc','area','imagem_logo']


class FormPublicacao_Grupo_de_Estudo(forms.ModelForm):
	
	class Meta:
		model = Publicacao_Grupo_de_Estudo
		fields = ['titulo','texto','anexo','area']


class FormComent_Publicacao_Grupo_de_Estudo(forms.ModelForm):

	class Meta:
		model = Coment_Publicacao_Grupo_de_Estudo
		fields = ['coment']

class Forum_Duvida(forms.ModelForm):
	
	class Meta:
		model = Forum_Duvida
		fields = ['texto','area']

class RegisterForm(UserCreationForm):

	email = forms.EmailField(label = 'E-mail')
	first_name = forms.CharField(label = 'Primeiro Nome')
	last_name = forms.CharField(label = 'Sobrenome')

	def save(self,  commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user

class Publicacao(forms.ModelForm):

	class Meta:
		model = Publicacao
		fields = ['titulo','texto', 'anexo', 'area']

class Edit_User(forms.Form):

	class Meta:
		model = EditUser
		fields = ['last_name','first_name', 'email']

class CadAreaForm(forms.ModelForm):
	
	class Meta:
		model = Obt_Estudo
		fields = ['nome']

class Coment_Publi(forms.ModelForm):
	
	class Meta:
		model = Coment_Publi
		fields = ['coment']

class Resp_Forum_Duvida(forms.ModelForm):
	
	class Meta:
		model = Resp_Forum_Duvida
		fields = ['resp']