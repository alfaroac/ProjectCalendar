from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Institution

@login_required
def calendar(request):
	return render(request,'index.html')

def institucion(request):
	instituciones=Institution.objects.all()

	return render(request,'informes/institucion.html', {"instituciones":instituciones})


