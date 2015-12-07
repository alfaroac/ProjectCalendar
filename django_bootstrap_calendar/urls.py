# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from .views import CalendarJsonListView, CalendarView, CrearEvento

urlpatterns = [
  url(r'^json/$',login_required(CalendarJsonListView.as_view()), name='calendar_json'),
  url(r'^$', login_required(CalendarView.as_view()), name='calendar'),
  url(r'^crear_evento$', login_required(CrearEvento.as_view()), name='crear_evento'),
  url(r'^datalle/(?P<evento_id>[0-9]+)/$', 'django_bootstrap_calendar.views.detalle_evento', name='detalle'),
  url(r'^delete/(?P<id>\d+)/$', 'django_bootstrap_calendar.views.delEvento', name='delEvento'),
  
  url(r'^evidencias/$','django_bootstrap_calendar.views.evidencias', name='evidence'),
  url(r'^evidencias/agregar/$','django_bootstrap_calendar.views.addEvidence', name='addEvidence'),
  url(r'^evidencias/editar/(?P<id>\d+)$','django_bootstrap_calendar.views.updEvidence',name='updEvidence'),
  url(r'^evidencias/eliminar/(?P<id>\d+)$','django_bootstrap_calendar.views.delEvidence',name='delEvidence'),

]
