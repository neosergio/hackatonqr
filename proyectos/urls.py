from django.conf.urls import patterns, url

from proyectos import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'proyectos_registrados/(?P<id_proyecto>\d+)/$', views.project, name='proyecto'),
	url(r'proyectos_registrados/(?P<id_proyecto>\d+)/inscribirse/$', views.register, name='register'),
)