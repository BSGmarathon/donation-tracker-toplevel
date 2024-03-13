import os

ALLOWED_HOSTS = ['localhost']
CSRF_TRUSTED_ORIGINS = ['http://localhost']
USE_X_FORWARDED_HOST = True

TRACKER_HAS_CELERY = False
TRACKER_PRIVACY_POLICY_URL = ''
TRACKER_SWEEPSTAKES_URL = ''
TRACKER_PAGINATION_LIMIT = 500
TRACKER_LOGO = ''
PAYPAL_TEST = True

# this is used as part of the auto-mailing services to identify where
# to redirect registration and password resets to
DOMAIN = 'localhost'

PAYPAL_DOMAIN = 'http://localhost'

# Leave this as true during development, so that you get error pages describing what went wrong
DEBUG = True

# You can add your e-mail if you want to receive notifications of failures I think , but its probably not a good idea
ADMINS = [
]

# You can also make local sqlite databases in your current directory 
# if you want to test changes to the data model
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': 'db/testdb',
  },
}

TIME_ZONE = 'Europe/Stockholm'

SITE_NAME = 'Demo Tracker'
SITE_NAME_SHORT = 'Demo'

# set this to your site's prefix, This allows handling multiple deployments from a common url base
SITE_PREFIX = '/'

SECRET_KEY = 'Replace This'

STATICFILES_DIRS = (
  # os.path.abspath('tracker/static/'),
  os.path.abspath('donation-tracker/tracker/static/'),
)

STATIC_URL = "/static" + SITE_PREFIX
STATIC_ROOT = "/var/www/html/static" + SITE_PREFIX

HAS_GDOC = False
# GDOC_USERNAME = 'person@gmail.com'
# GDOC_PASSWORD = '12345678'

HAS_EMAIL = False
#EMAIL_HOST = ''
#EMAIL_PORT = 465
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_FROM_USER = ''
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False


HAS_GOOGLE_APP_ID = False
# GOOGLE_CLIENT_ID = 'the.google.apps.url.thingy'
# GOOGLE_CLIENT_SECRET = 'secretpasswordthing'

HAS_GIANTBOMB_API_KEY = False
# GIANTBOMB_API_KEY = 'Itsreallynicetohaveanditsfreetomakeanaccountbutnotneccessary'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

USE_NEW_DONATE_LAYOUT = False

USE_AMQP = False
#AMQP_CONNECTIONSTRING = "amqps://username:password@mq.example.com/v_host"
