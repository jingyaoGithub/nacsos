import os

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = SECRET_KEY
SECRET_KEY = 12345

# Set debug true in development settings, and false in production
DEBUG = True

from fnmatch import fnmatch
class glob_list(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False

INTERNAL_IPS = glob_list([])

POSTGRES_EXTRA_DB_BACKEND_BASE = 'django.contrib.gis.db.backends.postgis'
#POSTGRES_EXTRA_DB_BACKEND_BASE = 'psqlextra.backend'

DATABASES = {
    'default': {
        #'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'ENGINE': 'psqlextra.backend',
        #'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'scoping_tmvv',
        'USER': 'postgres',
        'PASSWORD': 'Zjy980329',
        'HOST': 'localhost',
        'PORT': '',
    }
}
