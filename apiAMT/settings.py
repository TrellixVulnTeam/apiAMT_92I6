"""
Django settings for apiAMT project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

#from pathlib import Path
import os
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rx&i4mp6q!!qg1%$v8w1w)-d$w@i1#3xei1=19z@$m_$*+a_qw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

# if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
#    DEBUG = True
# else:
#    DEBUG = False

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = [
    'apiamt.herokuapp.com',
    '127.0.0.1',
    'localhost'
]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',

    'django_user_agents',

    'rest_framework',
    'rest_framework.authtoken',

    'corsheaders',

    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'capacity_summary_report',
    'conductor_sales_report',
    'corridor_performance_report',
    'CSVS.apps.CsvsConfig',
    'index_translation',
    'passenger_by_bus_and_trip_report',
    'settlement_file_operator',

]

# https://django-rest-auth.readthedocs.io/en/latest/introduction.html
SITE_ID = 1

SWAGGER_SETTINGS = {
	'SECURITY_DEFINITIONS': {
		"Auth Token": {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
		}
	}
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',

    'CSVS.middleware.SimpleMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.AllowAny',
    ],

    #'USER_DETAILS_SERIALIZER': 'userapp.serializer.UserDetailsSerializer',

    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        # 'PAGE_SIZE': 10
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# # Name of cache backend to cache user agents. If it not specified default
# # cache alias will be used. Set to `None` to disable caching.
# USER_AGENTS_CACHE = 'default'

REST_AUTH_SERIALIZERS = {
    # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
    'TOKEN_SERIALIZER': os.path.join('apiAMT.api.serializer.MyCustomTokenSerializer'),
}

ROOT_URLCONF = 'apiAMT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'apiAMT.wsgi.application'

CORS_ALLOWED_ORIGINS = [
    'https://famba-602ad.firebaseapp.com',
    'https://famba-602ad.web.app',
    'http://localhost:8100',
    'http://127.0.0.1:3306',
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

'''
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_amt',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_amt',
        'USER':'amt',
        'PASSWORD':'amt12345678',
        'HOST':'database-1.crpf0z5geewa.us-east-1.rds.amazonaws.com',
        'PORT':'5432'
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_amt',
        'USER':'postgres',
        'PASSWORD':'admin',
        'HOST':'localhost',
        'PORT':'5432'
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization en-us
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

#SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'kevenmariquel@gmail.com'
# EMAIL_HOST_PASSWORD = 'Abel@admin/2019'

# Teste site para teste>> https://mailtrap.io/
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '54a4afeca5896f'
EMAIL_HOST_PASSWORD = '22bc247d3b581c'
EMAIL_PORT = '2525'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())