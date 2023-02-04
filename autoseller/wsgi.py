# /var/www/erlankg1_pythonanywhere_com_wsgi.py

import os
import sys

path = '/home/erlankg1/autoseller'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'autoseller.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
