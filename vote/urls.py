from django.conf.urls import patterns, url

from vote import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
    url(r'(?P<id_candidate>\d+)/$', views.vote, name="candidate"),
    url(r'(?P<id_candidate>\d+)/confirmar$', views.confirm_vote, name="confirm"),
)