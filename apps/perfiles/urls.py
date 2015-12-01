from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^usuarios$', 'apps.perfiles.views.listaUsuarios', name='usuarios'),    
]
