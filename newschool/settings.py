"""
Django settings for newschool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Where manage.py is
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Where settings.py is
PROJECT_DIR = os.path.join(BASE_DIR, 'newschool')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'v*c3d#s6cu(r9c@1y+okbl*wh6vh77^w2pw0sgqf&rx!bads8f')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'on') != 'off'

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(';')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'roster',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'newschool.urls'

WSGI_APPLICATION = 'newschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'newschool.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)
