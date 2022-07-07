import os
from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
                       s.strip() for s in v.split(',')])
CORS_ORIGIN_ALLOW_ALL = config(
    "CORS_ORIGIN_ALLOW_ALL", default=False, cast=bool)
CORS_ORIGIN_WHITELIST = config("CORS_ORIGIN_WHITELIST").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'store',
    "hotel",
    "corsheaders"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CSRF_COOKIE_SECURE = False
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


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

DATE_INPUT_FORMATS = ['%d-%m-%Y']
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    # "DATE_INPUT_FORMATS": ["%d-%m-%Y",],
    # # 'DATE_FORMAT': ["%d-%m-%Y",],
    # # #'DATETIME_FORMAT': ["%d-%m-%Y %H:%M:%S",],

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',

    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
DJOSER = {
    "SEND_ACTIVATION_EMAIL": False,
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://test.localhost/"],
}

STATIC_URL = '/static/'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')

                    ]
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = BASE_DIR / 'media/'

# STRIPE, DATABASE CONFIGs
IN_PRODUCTION = config('USE_PRODUCTION_SETTINGS', default=False, cast=bool)

if IN_PRODUCTION:

    STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

    # DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': config('DB_NAME'),
    #     'USER': config('DB_USER'),
    #     'PASSWORD': config('DB_PASSWORD'),
    #     'HOST': config('DB_HOST'),
    # }
# }
else:
    STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
    STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
