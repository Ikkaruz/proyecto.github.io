"""
WSGI config for Proyecto_distribuidos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
#El archivo encargado de ser compatible con el servidor web.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_distribuidos.settings')

application = get_wsgi_application()
