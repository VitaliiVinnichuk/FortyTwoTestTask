from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^',
                           include('apps.person_info.urls')),
                       url(r'^admin/',
                           include(admin.site.urls)),
                       )
urlpatterns += staticfiles_urlpatterns()
