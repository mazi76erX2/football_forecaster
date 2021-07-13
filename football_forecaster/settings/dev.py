from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

"""""""""""""""""""""""""""""""""""""""""""""""""""""
                    CORS Headers
"""""""""""""""""""""""""""""""""""""""""""""""""""""

CORS_ORIGIN_WHITELIST = [
    'http://0.0.0.0:3000',
    'http://localhost:3000'
]

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
                Local Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

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
                Debug Toolbar
"""""""""""""""""""""""""""""""""""""""""""""""""""""

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

INSTALLED_APPS += [
    # third party
    'debug_toolbar',
]

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
