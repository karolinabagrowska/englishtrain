from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse


urlpatterns = patterns('',
   

   
   url(r'^activate/complete/$', direct_to_template, {'template': 'accounts/activation_complete.html'},
       name='accounts_activation_complete'),
   url(r'^register/complete/$', direct_to_template, {'template': 'accounts/registration_complete.html'},
       name='accounts_registration_complete'),
                       
   url(r'^login/$', 'django.contrib.auth.views.login', name='accounts_login'),
   url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='accounts_logout'),
   url(r'^activate/(?P<activation_key>\w+)/$', 'accounts.views.activate', name='accounts_activate'),
   url(r'^register/$', 'accounts.views.register', name='accounts_register'),
   
   url(r'^edit_profile/$', 'accounts.views.edit_profile', name='accounts_edit_profile'),
   
   url(r'^profile/(?P<username>[-_\.\w]+)/$', 'accounts.views.show_profile', name='accounts_show_profile'),

)
