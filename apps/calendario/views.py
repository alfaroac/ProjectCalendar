# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def calendar(request):
	return render(request,'index.html')

def actividad(request):
   return render(request,'calendar/actividad.html')
