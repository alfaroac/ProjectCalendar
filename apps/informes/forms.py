from django import forms
from .models import Institution, Informes

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
	# filename = forms.CharField(max_length=100)
	# docfile = forms.FileField(
 #        label='Selecciona un archivo'
 #    )
	class Meta:
		model=Informes
		exclude=()
		# widgets={
		
		# }	
		
