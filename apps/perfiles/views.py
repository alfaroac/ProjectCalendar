from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfiles
#from .forms import InstitucionForm

@login_required
def calendar(request):
	return render(request,'index.html')

def usuarios(request):
	return render(request,'perfil/usuarios.html')

def listaUsuarios(request):
	lista=Perfiles.objects.all()
	nro_registros=lista.count()
	return render(request,'perfil/usuarios.html', {"listUsers":lista, 'cantidad':nro_registros})
