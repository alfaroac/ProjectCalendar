from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Institution
from .forms import InstitucionForm

from django.core.urlresolvers import reverse

@login_required
def calendar(request):
	return render(request,'index.html')

def institucion(request):
	instituciones=Institution.objects.all()
	cantidad_registros=instituciones.count()
	return render(request,'informes/institucion.html', {"instituciones":instituciones, 'cantidad':cantidad_registros})

def crear_registro(request):
	if request.method=='POST':
		modelform=InstitucionForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:institucion'))
	else:
		modelform=InstitucionForm()

	return render(request,'informes/crear_registro.html', {'form':modelform})
			
	
