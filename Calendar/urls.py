"""Calendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
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
