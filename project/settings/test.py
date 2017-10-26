# flake8: noqa

from .base import *


DEBUG = True
SECRET_KEY = 'mykey'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}
