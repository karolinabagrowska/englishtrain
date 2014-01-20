"""
WSGI config for dupa project.
     
This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.
"""
NAME = 'englishtrain'


import os
import sys




paths = [#'/home/mario199/python_libs/django15/django', 
		'/home/mario199/python_libs/django15',
		#'/home/mario199/python_libs',
		'/home/mario199/python', 
		'/home/mario199/apps', 
		'/home/mario199/apps/%s' % NAME, ]

for i in paths:
	if i not in sys.path:
		sys.path.insert(0, i)

def application(environ, start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return ['<html><body>Hello World!</body></html>']

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % NAME)

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

#test
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#application = application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
