

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendario/', include('apps.calendario.urls', namespace='calendar_app')),
    url(r'^informes/', include('apps.informes.urls', namespace='informes_app')),
    url(r'^perfiles/', include('apps.perfiles.urls', namespace='perfiles_app')),
    url(r'^calendar/', include('django_bootstrap_calendar.urls', namespace='calendario_app')),
    url(r'^$', 'django.contrib.auth.views.login',{'template_name':'perfil/index.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name='logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    
   # url(r'^informes/', include('apps.informes.urls')), 
    #url(r'^$', include('apps.perfiles.urls')),
]
