from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView 
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', RedirectView.as_view(url='/index/')),
	url(r'^index/$', 'ampta_app.views.index', name="index"),
   
    #####login
    url(r'^login/$', 'ampta_app.views.login_user', name="login"),
    url(r'^logout/$', 'ampta_app.views.logout_user', name="logout"),

    #####projects
    url(r'^projects/$', 'ampta_app.views.project_list', name="project_list"),
    url(r'^project/add$', 'ampta_app.views.project_add', name="project_add"),
    url(r'^project/(?P<project_id>\d+)/show/$', 'ampta_app.views.project_show', name="project_show"),
    url(r'^project/(?P<project_id>\d+)/delete/$', 'ampta_app.views.project_delete', name="project_delete"),
    url(r'^project/(?P<project_id>\d+)/confirm_delete/$', 'ampta_app.views.project_confirm_delete', name="project_confirm_delete"),
    url(r'^project/(?P<project_id>\d+)/edit/$', 'ampta_app.views.project_edit', name="project_edit"),
     url(r'^projects/filter$', 'ampta_app.views.project_filter', name="project_filter"),
    #####tickets
    
    url(r'^ticket/(?P<project_id>\d+)/add/$', 'ampta_app.views.ticket_add', name="ticket_add"),
    url(r'^ticket/(?P<ticket_id>\d+)/edit/$', 'ampta_app.views.ticket_edit', name="ticket_edit"),
    url(r'^ticket/(?P<ticket_id>\d+)/show/$', 'ampta_app.views.ticket_show', name="ticket_show"),
    url(r'^ticket/(?P<ticket_id>\d+)/delete/$', 'ampta_app.views.ticket_delete', name="ticket_delete"),
    url(r'^ticket/(?P<ticket_id>\d+)/confirm_delete/$', 'ampta_app.views.ticket_confirm_delete', name="ticket_confirm_delete"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
   
    url(r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
    url(r'^admin/', include(admin.site.urls)),

)
