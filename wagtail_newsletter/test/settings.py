"""
Django settings for temp project.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/stable/ref/settings/
"""

import os

from django.conf import settings
import dj_database_url  # Add this import at the top


# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "not-a-secure-key"  # noqa: S105

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "testserver","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "wagtail_newsletter",
    "wagtail_newsletter.test",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.api.v2",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.styleguide",
    "wagtail.sites",
    "wagtail",
    "taggit",
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'blog'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "wagtail_newsletter.test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}


# don't use the intentionally slow default password hasher
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)


# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default="sqlite:///test_wagtail_newsletter.db"),
}


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "test-static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "test-media")


# Wagtail settings

WAGTAIL_SITE_NAME = "Wagtail Newsletter test site"

WAGTAIL_NEWSLETTER_RECIPIENTS_MODEL = "wagtail_newsletter_test.CustomRecipients"
WAGTAIL_NEWSLETTER_FROM_NAME = "Test Sender"
WAGTAIL_NEWSLETTER_REPLY_TO = "sender@example.com"

# Add these settings at the end of the file
WAGTAILADMIN_BASE_URL = "http://localhost:8000"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
