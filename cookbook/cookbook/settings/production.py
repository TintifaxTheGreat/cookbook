from decouple import config

DEBUG = False
WAGTAIL_PAGES_IS_CREATABLE = False

SECRET_KEY = config("SECRET_KEY")

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = ['localhost', 'cookbook.lindy.net']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

try:
    from .local import *
except ImportError:
    pass
