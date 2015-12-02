from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'apps.calendario.views.calendar', name='panel'),
    url(r'^institucion$', 'apps.informes.views.institucion', name='institution'),    
    url(r'^institucion/registro/nuevo/$', 'apps.informes.views.addInstitution', name='nuevo'),    
    url(r'^institucion/editar/(?P<id>\d+)$', 'apps.informes.views.editInstitution', name='edit'),    
    url(r'^delete/(?P<id>\d+)$', 'apps.informes.views.deleteInstitution', name='delete'),
    #url(r'^edit/(?P<pk>\d+)/$', ClienteUpdate.as_view(), name ='clientes_u'),
    #    url(r'^delete/(?P<pk>\d+)/$', ClienteDelete.as_view(), name ='clientes_d'),
]
