import os
from pathlib import Path
from pathlib import Path

import psycopg2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django1-insecure-c*k5o_86df1bafuusv*y^v2a71znfb=*vx!kim%p)s(0be83lb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['89.108.79.196']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cars.apps.CarsConfig',  # application for selling cars
    'credit.apps.CreditConfig',  # application for credit calculation
    'content.apps.ContentConfig',  # application for content
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'autoseller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # context processor for getting all brands
                'cars.context_processors.get_all_brands',
                # context processor for getting all vehicles types
                'cars.context_processors.get_all_vehicle_types',
                # context processor for getting all years
                'cars.context_processors.get_all_years',
                # context processor for getting all transmissions
                'cars.context_processors.get_all_transmissions',
                # context processor for getting trade in form
                'cars.context_processors.trade_in',
                # context processor for getting all drive units
                'cars.context_processors.get_all_drive_units',
                # context processor for getting phone numbers
                'content.context_processors.get_phone_numbers',
                'content.context_processors.get_email',  # context processor for getting email
                # context processor for getting address
                'content.context_processors.get_address',
                'content.context_processors.get_logo',  # context processor for getting logo
                # context processor for getting work time
                'content.context_processors.get_work_time',
                # context processor for getting all tech centers
                'content.context_processors.get_all_tech_centers',
                # context processor for getting whatsapp
                'content.context_processors.get_whatsapp',
                'content.context_processors.get_title',  # context processor for getting title
                'content.context_processors.get_dns',  # context processor for getting dns
                # context processor for getting banners
                'content.context_processors.get_banners',
                # context processor for getting all gifts
                'credit.context_processors.get_all_gifts',

            ],
        },
    },
]

WSGI_APPLICATION = 'autoseller.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'autoseller',
        'USER': 'userdb',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'  # path to static files
STATIC_ROOT = 'home/django/autoseller/static'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]  # for development server only (manage.py runserver)
# for development server only (manage.py runserver)

MEDIA_URL = 'media/'
MEDIA_ROOT = 'home/django/autoseller/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
