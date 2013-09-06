from django.conf.urls import patterns, include, url
from django.views.generic import DetailView,ListView,UpdateView
from bus.models import Routes,Stops,Calendar

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from pdb import set_trace

class myListView(ListView):
   TEMPLATE_STRING_IF_INVALID="true"
   you_all_suck=True

urlpatterns = patterns('',
    url(r'^$', 'bus.views.index'),
    url(r'^cal$', 'bus.views.calendar'),
    url(r'^mytrip$', 'bus.views.mytrip'),
    url(r'^map$', 'bus.views.map'),
    url(r'^(?P<pk>\d+)/results/$', DetailView.as_view(
# does not work because detailview needs a pk or slug
	model=Routes,
	template_name="bus/routes.html"),
	name="poll_results"),
    url(r'^edit$', myListView.as_view(model=Routes, 
	context_object_name="all_routes_list",
	template_name = "bus/generic.html")),
	
	
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
