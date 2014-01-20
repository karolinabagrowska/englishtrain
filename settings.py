# encoding: utf-8
import os


ADMINS = (
     ('Mariusz', 'mariusz.blaszczak@gmail.com'),
)

MANAGERS = ADMINS


SITENAME = 'englishtrain'

LOGIN_REDIRECT_URL = 'subs.views.index'

AUTH_PROFILE_MODULE = "account.UserProfile"







TIME_ZONE = 'Europe/Warsaw'


SITE_ID = 1


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))

MEDIA_ROOT = os.path.join(CURRENT_PATH, 'media')
STATIC_ROOT = os.path.join(CURRENT_PATH, 'static')


STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'


STATICFILES_DIRS = (
    os.path.join(CURRENT_PATH, 'static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SECRET_KEY = '(j*k0rgqc5ife8*tu@(3v*7)6bcu^wuw_x2ybq$vnd6!yo8)t-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'utils.context_processors.context_processors',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',    
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    
    
    'utils.middlewares.SetLanguageMiddleware',
    
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (

    os.path.join(CURRENT_PATH, 'templates'),
)


    
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',   
    'django.contrib.admin',
    
    


    'transmeta',
    'rosetta',
    'staticpage',
    'accounts',
    'subs',
    'utils',

    #'englishtrain.mptt', #parents management

)



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.



# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}




#LANGUAGE_CODE = 'pl'
TRANSMETA_DEFAULT_LANGUAGE  = 'en'
ugettext = lambda s: s 

LANGUAGES = (
    ('es', u'Español'),
    ('de', u'Deutsch'),
    ('en', u'English'),
)

TRANSMETA_LANGUAGES  = (
    ('es', ugettext('Spanish')),
    ('de', ugettext('German')),
    ('en', ugettext('English')),
)
USE_I18N = True

USE_L10N = True
LOCALE_PATHS = [os.path.join(CURRENT_PATH, 'locale'),]




ACCOUNT_ACTIVATION_DAYS = 7 




#from settings_development import *
from settings_production import *
