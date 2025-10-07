from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-in-production'
DEBUG = True
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nikhilpatidar151@gmail.com'   # temple official email
EMAIL_HOST_PASSWORD = 'odil qevq dsqq pxkc'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


# TWILIO_ACCOUNT_SID = "AC88f7bd3c4f035961ba77c6c9e6e6901b"
# TWILIO_AUTH_TOKEN = "9f91b24fc32596fef74492fe5ba247b0"
# TWILIO_VERIFY_SID = "VA56b14cbee8ac46c23cfae72d74b57658"
# TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
FAST2SMS_API_KEY = "Daq5RecMQAitsYyPBpS2FbZVfHdK7vwWNn3O9TUjzoGuIE1rk0hRwnYWfdVDNXuBtmcCk1sKM7SyjU8x"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vault',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mahapujadeposit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'vault' / 'templates'],
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

WSGI_APPLICATION = 'mahapujadeposit.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'vault' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Basic privacy: do not log Aadhar/phone values
import logging
class NoPIIFilter(logging.Filter):
    def filter(self, record):
        if record.args and isinstance(record.args, dict):
            for k in ('aadhaar_full','phone'):
                record.args.pop(k, None)
        return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': { 'no_pii': {'()': NoPIIFilter}},
    'handlers': {
        'console': { 'class': 'logging.StreamHandler', 'filters': ['no_pii'] }
    },
    'root': { 'handlers': ['console'], 'level': 'INFO' }
}
