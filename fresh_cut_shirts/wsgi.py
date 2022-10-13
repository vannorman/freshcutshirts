import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fresh_cut_shirts.settings.local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fresh_cut_shirts.settings.development')

application = get_wsgi_application()
