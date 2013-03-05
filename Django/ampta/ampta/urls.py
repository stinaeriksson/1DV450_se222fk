from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', 'ampta_app.views.index'),
    # Examples:
    # url(r'^$', 'ampta.views.home', name='home'),
    # url(r'^ampta/', include('ampta.foo.urls')),

    #####projects
    url(r'^projects/$', 'ampta_app.views.project_list', name="project_list"),
    #url(r'^project/add$', 'ampta_app.views.project_add', name="project_add"),
    #url(r'^project/(?P<project_id>\d+)/delete/$', 'ampta_app.views.project_delete', name="project_delete"),
    #url(r'^project/(?P<project_id>\d+)/edit/$', 'ampta_app.views.project_edit', name="project_edit"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
