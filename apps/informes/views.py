from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import Institution, Informes, Director
from .forms import InstitucionForm, InformeForm, DirectorForm

from django.core.urlresolvers import reverse

@login_required
def calendar(request):
	return render(request,'index.html')

@login_required
def institucion(request):
	instituciones=Institution.objects.all()
	cantidad_registros=instituciones.count()
	return render(request,'informes/institution.html', {"instituciones":instituciones, 'cantidad':cantidad_registros})

@login_required
def addInstitution(request):
	if request.method=='POST':
		modelform=InstitucionForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:institution'))
	else:
		modelform=InstitucionForm()

	return render(request,'informes/addInstitution.html', {'form':modelform})

@login_required
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

@login_required	
def deleteInstitution(request, id, template_name='informes/delInstitution.html'):
    obj_delete = Institution.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('informes_app:institution'))
    return render(request, template_name, {'object':obj_delete})

# informes
@login_required
def informes(request):
	obj_inf=Informes.objects.all()
	cantidad=obj_inf.count()
	return render(request,'informes/informes.html', {"informes":obj_inf, 'cantidad':cantidad})

@login_required
def addInforme(request):
	if request.method=='POST':
		modelform=InformeForm(request.POST,request.FILES)
		if modelform.is_valid():
			# modelform=Informes()
			modelform.save()
			return redirect(reverse('informes_app:informe'))
	else:
		modelform=InformeForm()
	return render(request,'informes/addInforme.html',{'form':modelform})
@login_required
def updateInforme (request, id):
	obj_update=Informes.objects.get(pk=id)
	if request.method=='POST':
		modelform=InformeForm(request.POST, request.FILES, instance=obj_update) #ojo
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:informe'))
	else:
		modelform=InformeForm(instance=obj_update)
	return render(request,'informes/updInforme.html', {'form':modelform},context_instance = RequestContext(request))

@login_required
def deleteInforme(request, id, template_name='informes/delInforme.html'):
    obj_delete = Informes.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('informes_app:informe'))
    return render(request, template_name, {'object':obj_delete})


# director
@login_required
def director(request):
	obj_dir=Director.objects.all()
	cantidad=obj_dir.count()
	return render(request,'informes/director.html', {"manager":obj_dir, 'cantidad':cantidad})

@login_required
def addDirector(request):
	if request.method=='POST':
		modelform=DirectorForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:director'))
	else:
		modelform=DirectorForm()
	return render(request,'informes/addDirector.html',{'form':modelform})
@login_required
def updDirector (request, id):
	obj_update=Director.objects.get(pk=id)
	if request.method=='POST':
		modelform=DirectorForm(request.POST, instance=obj_update)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('informes_app:director'))
	else:
		modelform=DirectorForm(instance=obj_update)
	return render(request,'informes/updDirector.html', {'form':modelform},context_instance = RequestContext(request))

@login_required
def delDirector(request, id, template_name='informes/delDirector.html'):
    obj_delete = Director.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('informes_app:director'))
    return render(request, template_name, {'object':obj_delete})