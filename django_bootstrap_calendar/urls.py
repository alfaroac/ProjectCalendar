# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from .views import CalendarJsonListView, CalendarView, CrearEvento

urlpatterns = [
  url(r'^json/$', CalendarJsonListView.as_view(), name='calendar_json'),
  url(r'^$', CalendarView.as_view(), name='calendar'),
  url(r'^crear_evento$', CrearEvento.as_view(), name='crear_evento'),
  
  url(r'^evidencias/$','django_bootstrap_calendar.views.evidencias', name='evidence'),
  url(r'^evidencias/agregar/$','django_bootstrap_calendar.views.addEvidence', name='addEvidence'),
  url(r'^evidencias/editar/(?P<id>\d+)$','django_bootstrap_calendar.views.updEvidence',name='updEvidence'),
  url(r'^evidencias/eliminar/(?P<id>\d+)$','django_bootstrap_calendar.views.delEvidence',name='delEvidence'),
]
