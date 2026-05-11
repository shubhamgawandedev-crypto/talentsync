"""
Django settings for config project.
Production Ready TalentSync Settings
"""
import os
from pathlib import Path

from decouple import config


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = config('SECRET_KEY')

DEBUG = config(
    'DEBUG',
    default=False,
    cast=bool
)

ALLOWED_HOSTS = ['*']


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [

    # DJANGO APPS

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'django.contrib.sites',


    # THIRD PARTY APPS

    'rest_framework',

    'rest_framework_simplejwt',

    'corsheaders',

    'allauth',

    'allauth.account',

    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'allauth.socialaccount.providers.linkedin_oauth2',


    # CUSTOM APPS

    'users',

    'jobs',

    'applications',

    'dashboard',
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================================================
# ROOT URL CONFIG
# =========================================================

ROOT_URLCONF = 'config.urls'


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [

    {

        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [

            BASE_DIR / 'templates'
        ],

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


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = 'config.wsgi.application'


# =========================================================
# DATABASE - POSTGRESQL
# =========================================================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': config(
            'DB_NAME',
            default='talentsync'
        ),

        'USER': config(
            'DB_USER',
            default='postgres'
        ),

        'PASSWORD': config(
            'DB_PASSWORD',
            default='admin123'
        ),

        'HOST': config(
            'DB_HOST',
            default='127.0.0.1'
        ),

        'PORT': config(
            'DB_PORT',
            default='5433'
        ),
    }
}

# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [

    {

        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {

        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',

        'OPTIONS': {

            'min_length': 8,
        }
    },

    {

        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {

        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================================================
# CUSTOM USER MODEL
# =========================================================

AUTH_USER_MODEL = 'users.User'


# =========================================================
# AUTHENTICATION BACKENDS
# =========================================================

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
)


# =========================================================
# SITE ID
# =========================================================

SITE_ID = 1


# =========================================================
# ALLAUTH SETTINGS
# =========================================================

ACCOUNT_LOGIN_METHODS = {

    'email'
}

ACCOUNT_SIGNUP_FIELDS = [

    'email*',

    'username*',

    'password1*',

    'password2*',
]


ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    BASE_DIR / 'static'
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)


# =========================================================
# MEDIA FILES
# =========================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (

        'rest_framework.permissions.AllowAny',
    ),
}


# =========================================================
# CORS
# =========================================================

CORS_ALLOW_ALL_ORIGINS = True


# =========================================================
# EMAIL CONFIGURATION
# =========================================================

EMAIL_BACKEND = (
    'django.core.mail.backends.smtp.EmailBackend'
)

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = config(
    'EMAIL_HOST_USER'
)

EMAIL_HOST_PASSWORD = config(
    'EMAIL_HOST_PASSWORD'
)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# =========================================================
# SECURITY SETTINGS
# =========================================================

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = False

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'


# =========================================================
# CACHE
# =========================================================

CACHES = {

    'default': {

        'BACKEND':
        'django.core.cache.backends.locmem.LocMemCache',
    }
}


# =========================================================
# DEFAULT AUTO FIELD
# =========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'