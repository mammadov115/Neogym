from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'db.sqlite3'
    }
}


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "uploads"