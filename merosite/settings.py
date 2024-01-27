import os
import logging.config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authenticate.apps.AuthenticateConfig',
    'contact.apps.ContactConfig',
    'account.apps.AccountConfig',
    'crispy_forms',
    'crispy_bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'merosite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'merosite.util.context_processors.site_information',
            ],
        },
    },
]

WSGI_APPLICATION = 'merosite.wsgi.application'


DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': os.environ.get('DB_NAME'),
      'USER': os.environ.get('DB_USER'),
      'PASSWORD': os.environ.get('DB_PASSWORD'),
      'HOST': os.environ.get('DB_HOST'),
      'PORT': os.environ.get('DB_PORT'),
   }
}
print(os.environ.get('DB_HOST'))

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# custom user model
AUTH_USER_MODEL = 'authenticate.CustomUser'

LOGIN_REDIRECT_URL = "account"
LOGOUT_REDIRECT_URL = "index"

# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = int(os.environ.get('EMAIL_TIMEOUT'))
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

SERVER_EMAIL = DEFAULT_FROM_EMAIL
ADMINS = [('System Administrator', SERVER_EMAIL)]

# context_processors of site information
SITE_INFORMATION = {
    'NAME': 'Merosite',
    'ADDRESS': '123 Heaven Drive, Universe, 12345',
    'PHONE': '123-456-7890',
    'EMAIL_PREFIX': 'support',
    'DESCRIPTION': 'Web Application',
    'CONTACT_US_EMAIL': DEFAULT_FROM_EMAIL,
}

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Logging
LOGGING_CONFIG = None
LOG_NAME = "application.log"
LOG_PATH =  BASE_DIR / "logs" / LOG_NAME
CONSOLE_LOG_LEVEL = "INFO"
APPS_LOG_LEVEL = "INFO"

LOGGING_DICT = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "short_message":{
            "format": "{asctime} {levelname} {message}",
            "style": "{",
        },
        "long_message": {
            "format": "{asctime} {process:d} {levelname} {module} {filename} {funcName} {pathname} Line#:{lineno:d} Message:{message}",
            "style": "{",
        }
    },
    "handlers": {
        "console":{
            "level": CONSOLE_LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "short_message",
        },
        "file": {
            "level": APPS_LOG_LEVEL,
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "midnight",
            "interval": 1,
            "filename": LOG_PATH,
            "formatter": "long_message",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "email_backend": EMAIL_BACKEND,
        }
    },
    "loggers": {
        "django":{
            "handlers": ["console", "file"],
            "level": APPS_LOG_LEVEL,
            "propagate": False,
        },        
        "django.request": {
            "handlers": ["file", "mail_admins"],
            "level": "INFO",
            "propagate": False,
        },
        "application": {
            "handlers": ["console", "file"],
            "level": APPS_LOG_LEVEL,
            "propagate": False,
        },
    }
}
logging.config.dictConfig(LOGGING_DICT)