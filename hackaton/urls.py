from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('proyectos.urls', namespace='proyectos')),
    url(r'^vote/', include('vote.urls', namespace='vote')),
    url(r'^admin/', include(admin.site.urls)),
)
