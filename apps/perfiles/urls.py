from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from .views import userRegister

urlpatterns = [
    url(r'^$', 'apps.perfiles.views.calendar', name='panel'),
    url(r'^usuarios$', 'apps.perfiles.views.listaUsuarios', name='users'),
    url(r'^registrar$', login_required(userRegister.as_view()), name='addUsers'),   
    url(r'^usuarios/editar/(?P<id>\d+)$', 'apps.perfiles.views.editUsers', name='edit'),     
    url(r'^usuarios/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.deleteUsers', name='delete'),
    
    url(r'^rol$','apps.perfiles.views.role', name='role'),
    url(r'^rol/add$','apps.perfiles.views.addRole',name='addRole'),
    url(r'^rol/editar/(?P<id>\d+)$', 'apps.perfiles.views.updateRole', name='updRole'),     
    url(r'^rol/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.deleteRole', name='delRole'),     
]
