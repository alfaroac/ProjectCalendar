from django import forms
from .models import CalendarEvent, Evidences
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets  
CSS_CLASS_CHOICES = (
        ('', _('Seleccione')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    
class EventForm(forms.ModelForm):
	css_class = forms.ChoiceField(CSS_CLASS_CHOICES)
	#start = forms.DateField(input_formats=['%d/%m/%Y'],
     #   widget=DateTimePicker(options={"format": "DD/M/YYYY HH:mm",
       #                                "pickSeconds": False}))
	#end = forms.DateField(input_formats=['%d/%m/%Y'],
     #   widget=DateTimePicker(options={"format": "DD/MM/YYYY HH:mm",
      #                                 "pickSeconds": False}))
	class Meta:
		model=CalendarEvent
		fields = ['title', 'url', 'css_class','start','end','place','description']
		exclude=()
		widgets={
		'title':forms.TextInput(attrs={'class':'form-control col-md-6'}),
		'url':forms.TextInput(attrs={'class':'form-control'}),
		'css_class':forms.TextInput(attrs={'class':'btn btn-primary'}),
		#'start':forms.DateField(attrs={'class':'form-control'}),
		#'end':forms.TextInput(attrs={'class':'form-control'}),
		'place':forms.TextInput(attrs={'class':'form-control'}),
		'description':forms.TextInput(attrs={'class':'form-control'}),
		}

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		self.fields['start'].widget = widgets.AdminSplitDateTime()
		self.fields['end'].widget = widgets.AdminSplitDateTime()

class EvidenceForm(forms.ModelForm):
	class Meta:
		model=Evidences
		exclude=()