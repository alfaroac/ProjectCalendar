from django.conf.urls import url



urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^actividad$', 'apps.calendario.views.actividad', name='actividad'),

]
