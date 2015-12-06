from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.template import RequestContext
from .models import Perfiles, Rol
from .forms import UserForm, RoleForm 

@login_required
def calendar(request):
	return render(request,'index.html')


def listaUsuarios(request):
	lista=Perfiles.objects.all()
	nro_registros=lista.count()
	return render(request,'users/users.html', {"lista":lista, 'cantidad':nro_registros})

class userRegister(FormView):
	template_name='users/addUsers.html'
	form_class=UserForm
	success_url=reverse_lazy('perfiles_app:users')

	def form_valid(self, form):
		user=form.save()
		perfil=Perfiles()
		perfil.usuario=user
		perfil.dni=form.cleaned_data['dni']
		perfil.rol=form.cleaned_data['rol']
		perfil.sexo=form.cleaned_data['sexo']
		perfil.direccion=form.cleaned_data['direccion']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.estado=form.cleaned_data['estado']
		perfil.imagen=form.cleaned_data['imagen']
		perfil.save()
		return super(userRegister,self).form_valid(form)

def editUsers(request, id):
	obj_edit=Perfiles.objects.get(pk=id)
	if request.method=='POST':
		formulario=UserForm(request.POST, instance=obj_edit)
		if formulario.is_valid():
			formulario.save()
			return redirect(reverse('perfiles_app:users'))
	else:
		formulario=UserForm(instance=obj_edit)
	return render(request,'users/updUsers.html', {'form':formulario},context_instance = RequestContext(request))
	
def deleteUsers(request, id, template_name='users/delUser.html'):
    obj_delete = Perfiles.objects.get(pk=id)    
    if request.method=='POST':
        obj_delete.delete()
        return redirect(reverse('perfiles_app:users'))
    return render(request, template_name, {'object':obj_delete})


# roles
def role(request):
	obj_rol=Rol.objects.all()
	cantidad=obj_rol.count()
	return render(request, 'users/role.html', {'roles':obj_rol,'cantidad':cantidad})

def addRole(request):
	if request.method=='POST':
		objform=RoleForm(request.POST)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:role'))
	else:
		objform=RoleForm()
	return render(request, 'users/addRole.html',{'form':objform})


def updateRole(request, id):
	obj_edit=Rol.objects.get(pk=id)
	if request.method=='POST':
		objform=RoleForm(request.POST, instance=obj_edit)
		if objform.is_valid():
			objform.save()
			return redirect(reverse('perfiles_app:role'))
	else:
		objform=RoleForm(instance=obj_edit)
	return render(request,'users/updRole.html', {'form':objform},context_instance = RequestContext(request))
	
def deleteRole(request, id, template_name='users/delRole.html'):
    server = Rol.objects.get(pk=id)    
    if request.method=='POST':
        server.delete()
        return redirect(reverse('perfiles_app:role'))
    return render(request, template_name, {'object':server})