import atexit
import os
import tempfile

tmpdir = tempfile.TemporaryDirectory()
os.environ.setdefault('DATA_DIR', tmpdir.name)

from pretalx.settings import *  # NOQA

DATA_DIR = tmpdir.name
LOG_DIR = os.path.join(DATA_DIR, 'logs')
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

atexit.register(tmpdir.cleanup)

EMAIL_BACKEND = 'django.core.mail.outbox'

COMPRESS_ENABLED = COMPRESS_OFFLINE = False
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

# Disable celery
CELERY_ALWAYS_EAGER = True
HAS_CELERY = False

# Don't use redis
SESSION_ENGINE = "django.contrib.sessions.backends.db"
HAS_REDIS = False
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
