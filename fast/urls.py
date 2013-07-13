from django.conf.urls import patterns, include, url
from pdb import set_trace

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#set_trace()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fast.views.home', name='home'),
    # url(r'^fast/', include('fast.foo.urls')),
    url(r'^bus/', include('bus.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
