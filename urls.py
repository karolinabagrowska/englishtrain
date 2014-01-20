from django.conf.urls.defaults import *
from settings import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.shortcuts import redirect

admin.autodiscover()
    
    

urlpatterns = patterns('',
                       

    
    url(r'^$', 'views.home_page', name='home_page'),
    #url(r'^$', direct_to_template, {'template': 'index.html'}, name='home_page'),
    url(r'^contact/$', direct_to_template, {'template': 'contact.html'}, name='contact'),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    
    
    


    
    url(r'^subs/', include('subs.urls')),
    url(r'^admin/rosetta/', include('rosetta.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  lambda x: redirect('add_subs')), 
    
    
    
   
    
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': MEDIA_ROOT,}),               
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT,}),
    
    
)





