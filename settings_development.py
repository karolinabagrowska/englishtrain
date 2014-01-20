from settings import *
DEBUG = TEMPLATE_DEBUG = True
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'englishtrain',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'tracer',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATIC_ROOT = ''
MEDIA_URL = 'http://127.0.0.1:8000/media/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mariusz.blaszczak@gmail.com'
EMAIL_HOST_PASSWORD = 'LogramosEncender'
DEFAULT_FROM_EMAIL = 'mariusz.blaszczak@gmail.com'