from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Rol, Perfiles

SEX = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

class UserForm(UserCreationForm):	
	rol = forms.ModelChoiceField(queryset=Rol.objects.all(),required=True)
	dni = forms.CharField(max_length=8)
	telefono = forms.CharField(max_length=13)
	sexo=forms.ChoiceField(SEX)
	direccion=forms.CharField(max_length=70)
	estado=forms.BooleanField()
	imagen=forms.ImageField()
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'rol', 'dni', 'telefono', 'sexo','direccion','estado','imagen')

# class UserRegisterForm(forms.ModelForm):
# 	class Meta:
			