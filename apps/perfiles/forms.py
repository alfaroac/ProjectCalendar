from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rol, Perfiles

class UsersForm(UserCreationForm):
	class Meta:
		model=User
 		exclude=()
 		widgets={
 		'username':forms.TextInput(attrs={'class':'form-control'}),
 		'user':forms.TextInput(attrs={'class':'form-control'}),
 		'first_name':forms.TextInput(attrs={'class':'form-control'}),
 		'last_name':forms.TextInput(attrs={'class':'form-control'}),
 		'email':forms.EmailInput(attrs={'class':'form-control'}),
 		'password':forms.TextInput(attrs={'class':'form-control'}),
 		}

SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

class PerfilForm(forms.ModelForm):		
	class Meta:
		#model=User
		model=Perfiles
		exclude=()
		widgets={
		#'usuario':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'dni':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		#'imagen':forms.FileInput(attrs={'class':'btn btn-warning'}),
		}


class RoleForm(forms.ModelForm):
	class Meta:
		model=Rol
		exclude=()
		widgets={
		'rol':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.Textarea(attrs={'rows': 5, 'cols': 100}),
		}
		
		
			
	
