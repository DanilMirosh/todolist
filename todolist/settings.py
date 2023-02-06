from pathlib import Path
from typing import Any

from envparse import env

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE_PATH = BASE_DIR.joinpath('.env')

if ENV_FILE_PATH.is_file():
    env.read_envfile(path=ENV_FILE_PATH)

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'social_django',
    'django_filters',
    # Project apps
    'todolist.core',
    'todolist.goals',
    'todolist.bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'todolist.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST', default='127.0.0.1'),
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

LOGGING: dict[str, Any] = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'health-check': {
            '()': 'todolist.filters.HealthCheckFilter',
        },
    },
    'formatters': {
        'console': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m--%d %H:%M:%S',
        },
        'sample': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s',
            'datefmt': '%Y-%m--%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['health-check'],
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'project': {
            'level': 'DEBUG',
            'filters': ['health-check'],
            'class': 'logging.StreamHandler',
            'formatter': 'sample',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['project'],
        },
        'django.server': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    }
}

if env.bool('SQL_ECHO', False):
    LOGGING['loggers'].update({
        'django.db': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    })

# Social Oauth
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_JSONFIELD_CUSTOM = 'django.db.models.JSONField'
SOCIAL_AUTH_VK_OAUTH2_KEY = env.str('VK_OAUTH2_KEY')
SOCIAL_AUTH_VK_OAUTH2_SECRET = env.str('VK_OAUTH2_SECRET')
AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_EXTRA_DATA = [('email', 'email')]
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

BOT_TOKEN = env.str('BOT_TOKEN')
