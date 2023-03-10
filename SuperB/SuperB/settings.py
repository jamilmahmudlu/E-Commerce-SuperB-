"""
Django settings for SuperB project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import datetime
from datetime import timedelta

import django

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p*0#p7^nyq0ns@n0x!-_(@^m=o=h*=0&j%&zjlt(de)rc5g8s@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'jet',

    # Priority Third Party apps
    'modeltranslation',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    # 'django.contrib.flatpages'
    # 'django.contrib.sites',


    # Third Party apps
    'ckeditor',
    'rosetta',
    'rest_framework',
    
    # Custom Apps
    'blog',
    'core',
    'order',
    'product',
    'user',
    'api',
    'social_django',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'SuperB.middleware.RequestLogMiddleware',
    'SuperB.middleware.IPAddressMiddleware',
    'django_country2.middleware.CountryMiddleware',


    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'SuperB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.get_subscriber_form',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.facebook.FacebookOAuth2',
#     'social_core.backends.google.GoogleOAuth2',

#     'django.contrib.auth.backends.ModelBackend',
# )

WSGI_APPLICATION = 'SuperB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'superbdb',
        'USER': 'superbuser',
        'PASSWORD': '23c1859fe6a04ba09b9afdcd2da96731',
        'HOST' : 'localhost',
        'PORT' : 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

from django.utils.translation import ugettext_lazy as _

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', _('English')),
    ('az', _('Az??rbaycan dili'))
)

LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_COOKIE_NAME = 'django_language'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

LOGS_ROOT = BASE_DIR / f'logs/login/{datetime.date.today()}.log'

BLOCK_ROOT = BASE_DIR / f'logs/blockip/{datetime.date.today()}.blockip'

STATICFILES_DIRS = [
    BASE_DIR / 'staticfiles',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

LOGIN_URL = 'login'
LOGIN_URL = '/auth/login/google-oauth2/'

LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '625127987891-ss4o7abmkathl6b7qoshs4mnqknm7ejn.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'user.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jamilmahmudlu@gmail.com'
EMAIL_HOST_PASSWORD = 'tgklfxsamojfihcx'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Baku'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
}