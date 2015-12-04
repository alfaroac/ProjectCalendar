from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
	
	codeInstitution=models.CharField(max_length=20, unique=True)
	nameInstitution = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	latitude = models.CharField(max_length=20, null=True)
	longitude = models.CharField(max_length=20, null=True)
	state=models.BooleanField()

class Informes(models.Model):
	institution = models.ForeignKey(Institution)
	nameFile = models.CharField(max_length=100)
	fileInform=models.FileField(upload_to='informes')
	description=models.TextField()
	dateLoad = models.DateTimeField(auto_now_add=True)
	
class Director(models.Model):
	yearWork=models.CharField(max_length=4)
	state=models.BooleanField()
	user = models.OneToOneField(User)
	institution = models.OneToOneField(Institution)
	
