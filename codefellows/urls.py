from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codefellows.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
