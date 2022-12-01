from .base import *

DEBUG = config('DEBUG', cast=bool)
# ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']
ALLOWED_HOSTS = [
    '143.198.79.233',
    'freshcutshirts.com',
    'www.freshcutshirts.com',
 ]


#AUTH_PASSWORD_VALIDATORS = [
#    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': config('DB_NAME'),
#        'USER': config('DB_USER'),
#        'PASSWORD': config('DB_PASSWORD'),
#        'HOST': config('DB_HOST'),
#        'PORT': ''
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
