import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fresh_cut_shirts.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fresh_cut_shirts.settings.production')

application = get_wsgi_application()
