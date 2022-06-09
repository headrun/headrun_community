"""
Django settings for Backpack project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT = os.environ.get('ENV_PROJECT', os.path.basename(BASE_DIR))
UI_DIR = os.path.join(BASE_DIR, '../dist')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('ENV_DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['*'] if DEBUG else list(set('.'.join(['']+x.rsplit('.', 2)[-2:]) for x in os.environ.get('ENV_SITES', '').split(' ')))


# Application List
APP_LIST = eval(os.environ.get('APP_LIST', '[]'))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
] + APP_LIST

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls.api'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [UI_DIR],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE':   'django.db.backends.postgresql_psycopg2',
#         'NAME':     os.environ.get('ENV_DATABASE_NAME', PROJECT + '_' + os.environ['SITE']).lower(),
#         'USER':     os.environ.get('ENV_DATABASE_USER', 'root1'),
#         'PASSWORD': os.environ.get('ENV_DATABASE_PASSWORD', 'root1'),
#         'HOST':     os.environ.get('ENV_DATABASE_HOST', 'localhost'),
#         'PORT':     os.environ.get('ENV_DATABASE_PORT', ''),
#         'OPTIONS':  {
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = True

USE_TZ = True

#Ind-time-zone on django-admin
TIME_ZONE =  'Asia/Kolkata'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    UI_DIR
]

AWS_STORAGE_BUCKET_NAME = os.environ.get('ENV_AWS_STORAGE_BUCKET_NAME')
if AWS_STORAGE_BUCKET_NAME and not DEBUG:
    AWS_ACCESS_KEY_ID = os.environ.get('ENV_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('ENV_AWS_SECRET_ACCESS_KEY')
    AWS_S3_SIGNATURE_VERSION =  os.environ.get('ENV_AWS_S3_SIGNATURE_VERSION', 's3v4')
    AWS_S3_REGION_NAME =  os.environ.get('ENV_AWS_S3_REGION_NAME', 'us-east-1')
    AWS_S3_FILE_OVERWRITE = os.environ.get('ENV_AWS_S3_FILE_OVERWRITE', False)
    AWS_DEFAULT_ACL = None
    AWS_S3_VERIFY = bool(os.environ.get('ENV_AWS_S3_VERIFY', False))

    DEFAULT_FILE_STORAGE = 'base.storages.MediaStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Log
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'file': {
#             'format': '%(asctime)s %(name)s:%(lineno)s %(levelname)s: %(process)d: %(message)s'
#         },
#         'loggly': {
#            'format': '{ "loggerName":"%(name)s", "timestamp":"%(asctime)s", "fileName":"%(filename)s", "logRecordCreationTime":"%(created)f", "functionName":"%(funcName)s", "levelNo":"%(levelno)s", "lineNo":"%(lineno)d", "time":"%(msecs)d", "levelName":"%(levelname)s", "message":"%(message)s"}',
#         }
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG' if DEBUG else 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'django.log'),
#             'formatter': 'file',
#         },
#         'loggly_logs': {
#                 'level': 'DEBUG' if DEBUG else 'INFO',
#                 'class': 'logging.handlers.SysLogHandler',
#                 'facility': 'local7',
#                 'formatter': 'loggly',
#                 'address' : '/dev/log',
#         },
#
#     },
#     'loggers': {
#         'loggly':{
#             'handlers': ['loggly_logs'],
#             'propagate': True,
#             'level': 'DEBUG' if DEBUG else 'INFO',
#         },
#         '': {
#             'handlers': ['file'],
#             'level': 'DEBUG' if DEBUG else 'INFO',
#             'propagate': True,
#         },
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG' if DEBUG else 'INFO',
#             'propagate': True,
#         },
#     },
# }

# Debug Toolbar
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
else:
    INSTALLED_APPS += [
        'django.contrib.sites',
    ]
    MIDDLEWARE += [
        'django.contrib.sites.middleware.CurrentSiteMiddleware',

        'base.middleware.APIMiddleware',
    ]

# rest_framework
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'base.api.views.exception_handler',
}
is_cors_enabled = os.environ.get("ENV_CORS_ALLOW_ALL_ORIGINS", False) or DEBUG
if is_cors_enabled:
    CORS_ALLOW_ALL_ORIGINS = True
    INSTALLED_APPS +=['corsheaders']
    # CorsMiddleware good to add before of CommonMiddleware on response/request.
    MIDDLEWARE.insert(2, "corsheaders.middleware.CorsMiddleware")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
