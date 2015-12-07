from django import forms
from .models import Institution, Informes, Director

class InstitucionForm(forms.ModelForm):
	class Meta:
		model=Institution
		#exclude=('latitude', 'longitude')
		exclude=()
		widgets={
		'codeInstitution':forms.TextInput(attrs={'class':'form-control col-md-6'}),
		'nameInstitution':forms.TextInput(attrs={'class':'form-control'}),
		'address':forms.TextInput(attrs={'class':'form-control'}),
		'latitude':forms.TextInput(attrs={'class':'form-control'}),
		'longitude':forms.TextInput(attrs={'class':'form-control'}),
		'state':forms.CheckboxInput(attrs={'class':'form-control'}),
		}

class InformeForm(forms.ModelForm):
	class Meta:
		model=Informes
		exclude=()
		widgets={
		'nameFile':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.TextInput(attrs={'class':'form-control'}),
		}	
		
class DirectorForm(forms.ModelForm):
	class Meta:
		model=Director
		exclude=()
		widgets={
		'yearWork':forms.TextInput(attrs={'class':'form-control'}),
		}