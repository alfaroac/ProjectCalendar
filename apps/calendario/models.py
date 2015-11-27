from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
#from utils import datetime_to_timestamp

class Activity(models.Model):

	CSS_CLASS_CHOICES = (
        ('', _('Normal')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )	
	title=models.CharField(max_length=100,unique=True)
	description = models.TextField()
	place = models.CharField(max_length=100)
	start=models.DateTimeField()
	end=models.DateTimeField()
	priority=models.CharField(blank=True, max_length=20, verbose_name=_('CSS Class'),
                                 choices=CSS_CLASS_CHOICES)
	organizer=models.ForeignKey(settings.AUTH_USER_MODEL)
