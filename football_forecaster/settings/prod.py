from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False
ALLOWED_HOSTS = ['*']

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                    Database
"""""""""""""""""""""""""""""""""""""""""""""""""""""

import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                    Sentry
"""""""""""""""""""""""""""""""""""""""""""""""""""""

SENTRY_DNS = os.environ.get('SENTRY_DNS')

sentry_sdk.init(
    dsn=SENTRY_DNS,
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

"""""""""""""""""""""""""""""""""""""""""""""""""""""
        Memcache Settings but must change to redis
"""""""""""""""""""""""""""""""""""""""""""""""""""""

# Memcached and pylibmc

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                    DataDog Configuration
"""""""""""""""""""""""""""""""""""""""""""""""""""""

INSTALLED_APPS += [
    'ddtrace.contrib.django',
]

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                Webpack Loader
"""""""""""""""""""""""""""""""""""""""""""""""""""""

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                Whitenoise
"""""""""""""""""""""""""""""""""""""""""""""""""""""

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                CSFR Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                    CORS Headers
"""""""""""""""""""""""""""""""""""""""""""""""""""""

CORS_ORIGIN_WHITELIST = [
    'http://0.0.0.0:3000',
    'http://localhost:3000'
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
