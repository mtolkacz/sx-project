from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_variable('SQL_DATABASE'),
        'USER': get_env_variable('SQL_USER'),
        'PASSWORD': get_env_variable('SQL_PASSWORD'),
        'HOST': get_env_variable('SQL_HOST'),
        'PORT': get_env_variable('SQL_PORT'),
    }
}

# disabling the browseable API in production
REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
})
