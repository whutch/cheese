# -*- coding: utf-8 -*-
"""Django settings."""
# Part of Cheese (https://github.com/whutch/cheese)
# :copyright: (c) 2015 Will Hutcheson
# :license: MIT (https://github.com/whutch/cheese/blob/master/LICENSE.txt)
"""
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Don't turn these on here, override them in local.py
DEBUG = False
TEMPLATE_DEBUG = False


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Optional apps
    "django.contrib.humanize",
    # Local apps
    "cheese.apps.core",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "unslashed.middleware.RemoveSlashMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "cheese.urls"

WSGI_APPLICATION = "cheese.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "cheese", "static"),
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)


# Templates

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "cheese", "templates"),
]


# Miscellaneous options

APPEND_SLASH = False
REMOVE_SLASH = True


# Bring in sensitive or non-portable settings from a non-versioned file

try:
    from .local import *
except ImportError:
    pass
