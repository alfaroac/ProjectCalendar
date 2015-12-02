from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Institution
from .forms import InstitucionForm

from django.core.urlresolvers import reverse

@login_required
def calendar(request):
	return render(request,'index.html')

def institucion(request):
	instituciones=Institution.objects.all()
	cantidad_registros=instituciones.count()
	return render(request,'informes/institution.html', {"instituciones":instituciones, 'cantidad':cantidad_registros})

def addInstitution(request):
	if request.method=='POST':
		modelform=InstitucionForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:institution'))
	else:
		modelform=InstitucionForm()

	return render(request,'informes/addInstitution.html', {'form':modelform})

def editInstitution (request, id):
	obj_edit=Institution.objects.get(pk=id)
	if request.method=='POST':
		formulario=InstitucionForm(request.POST, instance=obj_edit)
		if formulario.is_valid():
			formulario.save()
			return redirect(reverse('informes_app:institution'))
	else:
		formulario=InstitucionForm(instance=obj_edit)
	return render(request,'informes/updInstitution.html', {'form':formulario},context_instance = RequestContext(request))


	
def deleteInstitution (request, id):
    institution_delete = Institution.objects.get(pk=id)
    institution_delete.delete()
    return redirect(reverse('informes_app:institution'))	
	
