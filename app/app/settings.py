import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- GÜVENLİK ---
# Geliştirme ortamında varsayılan değerler atanmıştır
SECRET_KEY = os.environ.get('SECRET_KEY', 'devsecretkey')
DEBUG = bool(int(os.environ.get('DEBUG', 1))) # Geliştirmede varsayılan True

# Geliştirme ortamında docker-compose'daki ALLOWED_HOSTS'u al, yoksa hepsine izin ver
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '0.0.0.0,127.0.0.1,localhost,*').split(',')

# --- UYGULAMALAR ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',

    # Third Party Apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'imagekit',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
                'core.context_processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# --- VERİTABANI AYARLARI ---
# docker-compose.yml servisleri ile tam uyumlu hale getirildi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'devdb'),       # docker-compose: DB_NAME
        'USER': os.environ.get('DB_USER', 'devuser'),     # docker-compose: DB_USER
        'PASSWORD': os.environ.get('DB_PASS', 'changeme'), # docker-compose: DB_PASS
        'HOST': os.environ.get('DB_HOST', 'db'),           # docker-compose: DB_HOST
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- DİL VE ZAMAN ---
from django.utils.translation import gettext_lazy as _  # <--- BU SATIRI EKLE

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('tr', _('Turkish')),
    ('en', _('English')),
]

# Çeviri dosyalarının yolu (Ana dizinde 'locale' klasörü)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_COOKIE_NAME = 'django_language'

# --- DOSYA YOLLARI ---
STATIC_URL = '/static/static/'
STATIC_ROOT = '/vol/web/static'
MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/vol/web/media'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

# --- LOGGING ---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '{levelname} {message}', 'style': '{'},
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'simple'},
    },
    'loggers': {
        'app': {'handlers': ['console'], 'level': 'INFO', 'propagate': True},
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
    }
}

# --- GLOBAL PROJECT SETTINGS ---
PROJECT_NAME = "Django Project"
PROJECT_VERSION = "1.0.0"
CONTACT_INFO = {'phone': '+90 000 000 00 00', 'email': 'info@example.com', 'address': 'City, Country'}
SOCIAL_LINKS = {'github': 'https://github.com/emrefkrlr/'}
MAINTENANCE_MODE = False
SITE_ANNOUNCEMENT = None

# --- IMAGE PROCESSING ---
# docker-compose.yml'dan gelen ayarı doğru okur
WATERMARK_ENABLED = os.environ.get("WATERMARK_ENABLED", "False") == "True"
IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = 'imagekit.cachefiles.backends.Simple'

# --- ALLAUTH ---
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'optional'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID', ''),
            'secret': os.environ.get('GOOGLE_SECRET', ''),
            'key': ''
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_TOKEN_VARIABLE': 'JS_SDK'
    }
}