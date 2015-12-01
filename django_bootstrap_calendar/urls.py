# -*- coding: utf-8 -*-


from django.conf.urls import patterns, url
from .views import CalendarJsonListView, CalendarView, CrearEvento

urlpatterns = [
  url(r'^json/$', CalendarJsonListView.as_view(), name='calendar_json'),
  url(r'^$', CalendarView.as_view(), name='calendar'),
  url(r'^crear_evento$', CrearEvento.as_view(), name='crear_evento'),
]
