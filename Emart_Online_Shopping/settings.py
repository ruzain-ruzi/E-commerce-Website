"""
Django settings for Emart_Online_Shopping project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+*)cff3)0nwp7*o-s6(w1nbyt4--r0o0s05-f+n9i)4g=%s8bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'livereload',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cloudinary',
    'cloudinary_storage'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'livereload.middleware.LiveReloadScript',
]

ROOT_URLCONF = 'Emart_Online_Shopping.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Emart_Online_Shopping.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'HOST': "db.htctvkziatwakbkjegwp.supabase.co",
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "DQouuBOQMPENsdeg",
        'PORT': "5432"
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# DataFlair #Django #Static files
STATIC_URL = '/static/'
# --------------------------------------------------
# STATIC_ROOT = os.path.join(BASE_DIR, 'root')
# # -----------------------------------------------------
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'shop/static'),
# ]
STATICFILES_DIRS = os.path.join(BASE_DIR, 'shop/static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'shop/static')


import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "dni2bwk9n", 
  api_key = "947535293251513", 
  api_secret = "7VE4WU1pfgLPxMNhBuYBSc68KQ8" 
)

CLOUDINARY_STORAGE = {
  'CLOUD_NAME': "dni2bwk9n", 
  'API_KEY': "947535293251513", 
  'API_SECRET': "7VE4WU1pfgLPxMNhBuYBSc68KQ8" 
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
