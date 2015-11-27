from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse



@login_required
def calendar(request):
	return render(request,'index.html')

def actividad(request):
   return render(request,'calendar/actividad.html')

def crear_evento(request):
	if request.method=='POST':
		modelform=EventoForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect(reverse('calendar_app:actividad'))
	else:
		modelform=EventoForm()

	return render(request,'calendar/crear_evento.html', {'form':modelform})
			
