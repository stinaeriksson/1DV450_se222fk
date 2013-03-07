from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index/$', 'ampta_app.views.index', name="index"),
    # Examples:
    # url(r'^$', 'ampta.views.home', name='home'),
    # url(r'^ampta/', include('ampta.foo.urls')),

    #####login
    url(r'^login/$', 'ampta_app.views.login_user', name="login"),
    url(r'^logout/$', 'ampta_app.views.logout_user', name="logout"),
    url(r'^permission/error/$', 'ampta_app.views.error_permission', name="error_permission"),

    #####projects
    url(r'^projects/$', 'ampta_app.views.project_list', name="project_list"),
    url(r'^project/add$', 'ampta_app.views.project_add', name="project_add"),
    url(r'^project/(?P<project_id>\d+)/show/$', 'ampta_app.views.project_show', name="project_show"),
    url(r'^project/(?P<project_id>\d+)/delete/$', 'ampta_app.views.project_delete', name="project_delete"),
    url(r'^project/(?P<project_id>\d+)/edit/$', 'ampta_app.views.project_edit', name="project_edit"),
    #####tickets
    
    url(r'^ticket/(?P<project_id>\d+)/add/$', 'ampta_app.views.ticket_add', name="ticket_add"),
    #url(r'^ticket/(?P<ticket_id>\d+)/edit/$', 'ampta_app.views.ticket_edit', name="ticket_edit"),
    url(r'^ticket/(?P<ticket_id>\d+)/show/$', 'ampta_app.views.ticket_show', name="ticket_show"),
    #url(r'^ticket/(?P<ticket_id>\d+)/delete/$', 'ampta_app.views.ticket_delete', name="ticket_delete"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
