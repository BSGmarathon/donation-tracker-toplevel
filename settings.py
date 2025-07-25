# Django settings for donations project.

import os


try:
    import tracker_development.local as local
    print('Loaded normal settings')
except ImportError:
    try:
        import tracker_development.local_statics as local
        print('Loaded statics settings')
    except ImportError:
        import tracker_development.example_local as local

# new settings
TRACKER_HAS_CELERY = local.TRACKER_HAS_CELERY
TRACKER_PRIVACY_POLICY_URL = local.TRACKER_PRIVACY_POLICY_URL
TRACKER_SWEEPSTAKES_URL = local.TRACKER_SWEEPSTAKES_URL
TRACKER_PAGINATION_LIMIT = local.TRACKER_PAGINATION_LIMIT
TRACKER_LOGO = local.TRACKER_LOGO
PAYPAL_TEST = local.PAYPAL_TEST
MARATHON_ORG = local.MARATHON_ORG

BASE_DIR = os.path.dirname(__file__)

DEBUG = local.DEBUG

ALLOWED_HOSTS = local.ALLOWED_HOSTS
CSRF_TRUSTED_ORIGINS = local.CSRF_TRUSTED_ORIGINS

DOMAIN = local.DOMAIN
PAYPAL_DOMAIN = local.PAYPAL_DOMAIN

ADMINS = local.ADMINS

MANAGERS = ADMINS

DATABASES = local.DATABASES

SITE_PREFIX = 'tracker/'  # local.SITE_PREFIX

USE_X_FORWARDED_HOST = local.USE_X_FORWARDED_HOST
SECURE_PROXY_SSL_HEADER = local.SECURE_PROXY_SSL_HEADER

LOGIN_URL = SITE_PREFIX + 'user/login/'
LOGIN_REDIRECT_URL = SITE_PREFIX + 'user/index/'
LOGOUT_REDIRECT_URL = SITE_PREFIX + 'index/'

# Site name for admin headers
SITE_NAME = local.SITE_NAME

SITE_NAME_SHORT = local.SITE_NAME_SHORT

# Append slash seems to be the way to go overall
APPEND_SLASH = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = local.TIME_ZONE

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = local.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = local.STATIC_URL #'/static/'

print(local.STATIC_URL)

# Additional locations of static files
STATICFILES_DIRS = local.STATICFILES_DIRS

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = local.SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


SESSION_COOKIE_NAME = 'tracker_session'

ROOT_URLCONF = 'tracker_development.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tracker_development.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'post_office',
    'paypal.standard.ipn',
    'tracker',
    'rest_framework',
    'timezone_field',
    'mptt',
]

EMAIL_BACKEND = local.EMAIL_BACKEND

#You will also want to add the following to your server's crontab:
# * * * * * ($DONATIONS_LOCATION/manage.py send_queued_mail >> send_mail.log 2>&1)

# Pull in the tracker's lookup channels
ASGI_APPLICATION = 'tracker_development.routing.application'
CHANNEL_LAYERS = {'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'}}

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'tracker.auth.EmailLoginAuthBackend',
# )

# AUTH_PROFILE_MODULE = 'tracker.UserProfile'

if local.HAS_GDOC:
  GDOC_USERNAME = local.GDOC_USERNAME
  GDOC_PASSWORD = local.GDOC_PASSWORD

if local.HAS_EMAIL:
  EMAIL_HOST = local.EMAIL_HOST
  EMAIL_PORT = local.EMAIL_PORT
  EMAIL_HOST_USER = local.EMAIL_HOST_USER
  EMAIL_HOST_PASSWORD = local.EMAIL_HOST_PASSWORD
  MANDRILL_API_KEY = local.EMAIL_HOST_PASSWORD # the API key is the same as the SMTP password
  DEFAULT_FROM_EMAIL = local.EMAIL_FROM_USER
  EMAIL_FROM_USER = local.EMAIL_FROM_USER
  EMAIL_USE_TLS = local.EMAIL_USE_TLS
  EMAIL_USE_SSL = local.EMAIL_USE_SSL

if local.HAS_GOOGLE_APP_ID:
  GOOGLE_CLIENT_ID = local.GOOGLE_CLIENT_ID
  GOOGLE_CLIENT_SECRET = local.GOOGLE_CLIENT_SECRET

if local.HAS_GIANTBOMB_API_KEY:
  TRACKER_GIANTBOMB_API_KEY = local.GIANTBOMB_API_KEY

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
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
        },
#        'file': {
#            'level': 'ERROR',
#            'class': 'logging.FileHandler',
#            'filename': '/var/log/uwsgi/django-error.log',
#        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
