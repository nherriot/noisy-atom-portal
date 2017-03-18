"""
Django settings for noisyatom project.
Updated by Nicholas Herriot using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, socket

# A list of development machines that will make sure we use a 'non production' settings file. Add your machine name to
# the list to make this settings file a 'dev' build only.

DEVELOPER_MACHINES = ['Zenbook-UX32A', 'kieran', 'dilmac-VB', 'dilmac', 'my-mac-machine', 'my-linux-machine']


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xg6j41xd%uchs_j!5g0bvm4@!tt-mv^04@m*qlw#fa+q5cj)^*'

# SECURITY WARNING: don't run with debug turned on in production!
# Add your own computer name to this list of 'gethostname()' functions to get
# debug to true. Otherwise this will build a 'production' settings file.
if socket.gethostname() in DEVELOPER_MACHINES:
    print ("\n***** WARNING! This is a non-production build *****")
    DEBUG = True

    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
    # Setup the database as a developer machine.django.contrib.staticfiles
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': 'na_db',
            # 'USER': 'na_db_user',
            # 'PASSWORD': 'na_user',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_URL = '/static/'

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'cms.apps.CmsConfig',
    ]

# **************************************************************************************************************************
# ************************************ This section will be what the Live server runs **************************************
# **************************************************************************************************************************
else:

    print ("\n***** INFORMATION: PRODUCTION BUILD DEPLOYMENT *****")

    # Set allowed hosts so that we can verify where requests are coming from.
    ALLOWED_HOSTS = [
        'localhost',
        '127.0.0.1',
        'noisyatom.com',
        'noisyatom.co.uk',
        '104.236.14.123',
        ]

    DEBUG = False

    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
    # Setup the database as the production machine.
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'na_db_20022017',					# This is our database name
        'USER': 'na_db_user',						# This is the user of our database
        'PASSWORD': '9cobDTDa6N',						# This is the password of the database user
        'HOST': 'localhost',
        'PORT': '5432',
         }
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    #STATIC_URL = os.path.join(BASE_DIR, "static/")
    STATIC_URL = '/static-cdn/'


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'cms.apps.CmsConfig',
    ]

DEFAULT_FROM_EMAIL = "Noisy Atom <info@noisyatom.com>"

EMAIL_HOST = 'smtp.noisyatom.co.uk'
EMAIL_HOST_USER = 'support@noisyatom.co.uk'
EMAIL_HOST_PASSWORD = 'somepasswords'
EMAIL_PORT = 1025
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_URL = "http://noisyatom.com"

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]

# static_cdn stand for static content delivery network
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static-cdn')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media-cdn')

# crispy forms tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Registration package

# If True, users can register
REGISTRATION_OPEN = True

# One-week activation window; you may, of course, use a different value
ACCOUNT_ACTIVATION_DAYS = 7

# If True, the user will be automatically logged in.
REGISTRATION_AUTO_LOGIN = True

SITE_ID = 1

# The page you want users to arrive at after they successful log in
LOGIN_REDIRECT_URL = '/'
# The page users are directed to if they are not logged in,
# and are trying to access pages requiring authentication
LOGIN_URL = '/accounts/login/'
