from django import forms
from .models import Institution

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
		