

from django import forms
from .models import CalendarEvent

class EventForm(forms.ModelForm):
	class Meta:
		model=CalendarEvent
		#exclude=('latitude', 'longitude')
		exclude=()
		widgets={
		'title':forms.TextInput(attrs={'class':'form-control col-md-6'}),
		'url':forms.TextInput(attrs={'class':'form-control'}),
		'css_class':forms.TextInput(attrs={'class':'form-control'}),
		'start':forms.TextInput(attrs={'class':'form-control'}),
		'end':forms.TextInput(attrs={'class':'form-control'}),
		'place':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.TextInput(attrs={'class':'form-control'}),
		}
