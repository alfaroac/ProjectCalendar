from django.conf.urls import url

urlpatterns = [
    url(r'^institucion$', 'apps.informes.views.institucion', name='institution'),    
    url(r'^institucion/registro/nuevo/$', 'apps.informes.views.addInstitution', name='nuevo'),    
    url(r'^institucion/editar/(?P<id>\d+)$', 'apps.informes.views.editInstitution', name='edit'),    
    url(r'^delete/(?P<id>\d+)$', 'apps.informes.views.deleteInstitution', name='delete'),
    
    url(r'^informe/$','apps.informes.views.informes', name='informe'),
    url(r'^informes/add/$','apps.informes.views.addInforme', name='addInforme'),
    url(r'^informe/editar/(?P<id>\d+)$','apps.informes.views.updateInforme', name='updInforme'),
    url(r'^informe/eliminar/(?P<id>\d+)$','apps.informes.views.deleteInforme', name='delInforme'),

    url(r'^director/$','apps.informes.views.director',name='director'),
    url(r'^director/add/$','apps.informes.views.addDirector',name='addDirector'),
    url(r'^director/editar/(?P<id>\d+)$','apps.informes.views.updDirector',name='updDirector'),
    url(r'^director/eliminar/(?P<id>\d+)$','apps.informes.views.delDirector',name='delDirector'),
]
