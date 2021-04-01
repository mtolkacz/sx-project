from pathlib import Path
import os

from django.core.exceptions import ImproperlyConfigured

PROJECT_NAME = 'sx'
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = BASE_DIR / PROJECT_NAME

MEDIA_ROOT = ROOT_DIR / 'media_root'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static_root'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


def get_env_variable(var_name):
    """
    Get the environment variable or return exception.
    """
    try:
        return os.environ.get(var_name)
    except KeyError:
        error_msg = "Set s the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'rest_framework',

    # Local Apps
    'sx.zad1',
    'sx.zad2',
    'sx.core',  # common purpose utils
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'
