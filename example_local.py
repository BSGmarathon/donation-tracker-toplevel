import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'your.domain.name',
]
CSRF_TRUSTED_ORIGINS = ['http://localhost', 'https://your.domain.name']
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

TRACKER_HAS_CELERY = False
TRACKER_PRIVACY_POLICY_URL = ''
TRACKER_SWEEPSTAKES_URL = ''
TRACKER_PAGINATION_LIMIT = 500
TRACKER_LOGO = ''
PAYPAL_TEST = True

# this is used as part of the auto-mailing services to identify where
# to redirect registration and password resets to
DOMAIN = 'your.domain.name'

# Used by the Paypal integration for generating callback links.
# Should in almost all cases be the same as DOMAIN, but this allows you to customize if your environment requires it.
# Added when I had some issues with donations not working behind a reverse proxy due to bad link generation.
# Also allows you to direct paypal to go via a proxy service like ngrok for development while allowing you to still use localhost.
PAYPAL_DOMAIN = 'your.domain.name'

# Leave this as true during development, so that you get error pages describing what went wrong
DEBUG = True

# Site name for admin headers.  Change this for your own event.
SITE_NAME = 'Django'
SITE_NAME_SHORT = '<Your organization name here>'

# You can add your e-mail if you want to receive notifications of failures I think , but its probably not a good idea
ADMINS = [
	#('Your Name', 'your_email@example.com'),
]

# You can also make local sqlite databases in your current directory
# if you want to test changes to the data model
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  },
}

TIME_ZONE = 'Europe/Amsterdam'

# set this to your site's prefix, This allows handling multiple deployments from a common url base
SITE_PREFIX = '/'

# Generate a random value for this for your own site!  Used in session cookie generation, and some other things.
SECRET_KEY = 'GenerateARandomValueForThisForYourOwnSite'

STATICFILES_DIRS = (
  os.path.abspath('tracker/static/'),
)

STATIC_URL = "/static" + SITE_PREFIX
# STATIC_ROOT = os.path.join(BASE_DIR, 'static', SITE_PREFIX.lstrip('/'))
STATIC_ROOT = "/var/www/html/static" + SITE_PREFIX

HAS_GDOC = False
# GDOC_USERNAME = 'person@gmail.com'
# GDOC_PASSWORD = '12345678'

HAS_EMAIL = False
# EMAIL_HOST = 'mail.somwhere.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'dude@somewhere.com'
# EMAIL_HOST_PASSWORD = '1234567878'
# EMAIL_FROM_USER = 'someone_else@somewhere.com'

HAS_GOOGLE_APP_ID = False
# GOOGLE_CLIENT_ID = 'the.google.apps.url.thingy'
# GOOGLE_CLIENT_SECRET = 'secretpasswordthing'

HAS_GIANTBOMB_API_KEY = False
# GIANTBOMB_API_KEY = 'Itsreallynicetohaveanditsfreetomakeanaccountbutnotneccessary'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
