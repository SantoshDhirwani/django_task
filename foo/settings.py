import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'fk0d-3n1+7*oecn3p^_g4buf#-$haa!kaci12th&f_y!hmhp-7'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'foo.stonks',
]

ROOT_URLCONF = 'foo.urls'
WSGI_APPLICATION = 'foo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_new',
        'USER': 'admin',
        'PASSWORD': 'veenu12345',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
