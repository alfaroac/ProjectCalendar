from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from .views import addPerfil

urlpatterns = [
    url(r'^$', 'apps.perfiles.views.calendar', name='panel'),
    
    url(r'^users$', 'apps.perfiles.views.users', name='users'),
    url(r'^users/agregar/$','apps.perfiles.views.addUsers',name='addU_main'),
    url(r'^users/editar/(?P<id>\d+)$', 'apps.perfiles.views.updUser', name='updUser'),     
    url(r'^users/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.delUser', name='delUser'),

    url(r'^usuarios$', 'apps.perfiles.views.perfiles', name='perfil'),
    url(r'^registrar$', login_required(addPerfil.as_view()), name='addPerfil'),   
    url(r'^usuarios/editar/(?P<id>\d+)$', 'apps.perfiles.views.updPerfil', name='updPerfil'),     
    url(r'^usuarios/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.delPerfil', name='delPerfil'),
    

    url(r'^rol$','apps.perfiles.views.role', name='role'),
    url(r'^rol/add$','apps.perfiles.views.addRole',name='addRole'),
    url(r'^rol/editar/(?P<id>\d+)$', 'apps.perfiles.views.updateRole', name='updRole'),     
    url(r'^rol/eliminar/(?P<id>\d+)$', 'apps.perfiles.views.deleteRole', name='delRole'),     
]
