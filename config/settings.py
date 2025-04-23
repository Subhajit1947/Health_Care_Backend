
from pathlib import Path
from dotenv import load_dotenv
from os import getenv,path
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

APPS_DIR=BASE_DIR / "core_apps"
SECRET_KEY = 'django-insecure-ff7of4tfro)1nnbvkqj*p0ty6^1a&nx(ril@8pip6h#5g!3@!v'
local_env_file=path.join(BASE_DIR,".env")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0"
]


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

THIRD_PARTY_APPS=[
    "rest_framework",
]

LOCAL_APPS=[
    "core_apps.users",
    "core_apps.patients",
    "core_apps.doctors",
    "core_apps.mappings"
]


INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'users.User'  
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

COOKIE_NAME="access"
COOKIE_SAMESITE="Lax"
COOKIE_PATH="/"
COOKIE_HTTPONLY=True
COOKIE_SECURE=getenv("COOKIE_SECURE","True") == "True"
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":(
        "core_apps.common.cookie_auth.CookieAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES":(
        "rest_framework.permissions.IsAuthenticated",
    ),
}

SIMPLE_JWT={
    "SIGNING_KEY":getenv("SIGNING_KEY"),
    "ACCESS_TOKEN_LIFETIME":timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME":timedelta(days=1),
    "ROTATE_REFRESH_TOKEN":True,
    "USER_ID_FIELD":"id",
    "USER_ID_CLAIM":"user_id",
    'ALGORITHM': 'HS256',
}

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':getenv("POSTGRES_DB"),
        "USER":getenv("POSTGRES_USER"),
        "PASSWORD":getenv("POSTGRES_PASSWORD"),
        "HOST":getenv("POSTGRES_HOST"),
        "PORT":getenv("POSTGRES_PORT")
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
SITE_ID =1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=str(BASE_DIR/"staticfiles")


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
