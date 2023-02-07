import os
import psycopg2
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django1-insecure-c*k5o_86df1bafuusv*y^v2a71znfb=*vx!kim%p)s(0be83lb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

STATIC_URL = 'static/'  # path to static files
STATIC_ROOT = 'home/django/autoseller/static'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]  # for development server only (manage.py runserver)
# for development server only (manage.py runserver)
