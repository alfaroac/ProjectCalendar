from django.conf.urls import url

urlpatterns = [
    url(r'^institucion$', 'apps.informes.views.institucion', name='institution'),    
    url(r'^institucion/registro/nuevo/$', 'apps.informes.views.addInstitution', name='nuevo'),    
    url(r'^institucion/editar/(?P<id>\d+)$', 'apps.informes.views.editInstitution', name='edit'),    
    url(r'^delete/(?P<id>\d+)$', 'apps.informes.views.deleteInstitution', name='delete'),
    
]
