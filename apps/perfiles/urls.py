from django.conf.urls import include, url
from .views import userRegister

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^usuarios$', 'apps.perfiles.views.listaUsuarios', name='usuarios'),
    url(r'^registrar$', userRegister.as_view(), name='registrar_usuario'),    
]
