from django.conf.urls import patterns, url

from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),

	url(r'^(?P<pk>\d+)/$', views.DetailedProfile.as_view(), name='detail'),

	url(r'^create$', views.CreateAProfile.as_view(), name='create'),

	url(r'^delete/(?P<pk>\d+)/$', views.DeleteAProfile.as_view(), name='delete'),

	url(r'^edit/(?P<pk>\d+)/$', views.EditAProfile.as_view(), name='edit'),
)


