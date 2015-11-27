from django.db import models
from django.conf import settings

class Institution(models.Model):
	
	codeInstitution=models.CharField(max_length=20, unique=True)
	nameInstitution = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	state=models.BooleanField()

class Files(models.Model):
	institution = models.ForeignKey(Institution)
	nameFile = models.CharField(max_length=100)
	description=models.TextField()
	dateLoad = models.DateTimeField(auto_now_add=True)
	
class Manager(models.Model):
	yearWork=models.CharField(max_length=4)
	state=models.BooleanField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	institucion = models.ForeignKey(Institution)
	
