# -*- coding: utf 8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil,Obt_Estudo


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
		fields = ('imagem_perfil', 'bio',)


class CadAreaForm(forms.ModelForm):
	
	class Meta:
		model = Obt_Estudo
		fields = ['nome']
