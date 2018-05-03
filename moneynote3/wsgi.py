"""
WSGI config for moneynote3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
#sys.path.append('/home/ubuntu/Django')
#sys.path.append('/home/ubuntu/Django/bot')
#sys.path.append('/home/ubuntu/Django/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moneynote3.settings")

application = get_wsgi_application()
