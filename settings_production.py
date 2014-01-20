from settings import *
DEBUG = TEMPLATE_DEBUG = False
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mario199_la',                      # Or path to database file if using sqlite3.
        'USER': 'mario199_la',                      # Not used with sqlite3.
        'PASSWORD': 'YyJeLqeX',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATIC_ROOT = os.path.join(CURRENT_PATH, 'static')
MEDIA_URL = 'http://www.learnlangs.blaszczakphoto.com/media/'

DEFAULT_FROM_EMAIL = 'admin@learnlangs.blaszczakphoto.com'