from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles
from .forms import UserForm

@login_required
def calendar(request):
	return render(request,'index.html')

#def usuarios(request):
#	return render(request,'perfil/usuarios.html')

def listaUsuarios(request):
	lista=Perfiles.objects.all()
	nro_registros=lista.count()
	return render(request,'perfil/usuarios.html', {"lista":lista, 'cantidad':nro_registros})

class userRegister(FormView):
	template_name='perfil/registra_usuario.html'
	form_class=UserForm
	success_url=reverse_lazy('perfiles_app:usuarios')

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

