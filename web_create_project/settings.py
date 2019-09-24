"""
Django settings for web_create_project project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
# 9/16 import library
import django_heroku
from decouple import config
import whitenoise
import dj_database_url
# 9/16 import library

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY') # 9/17新增
# SECRET_KEY = '%4qakn%#z8ty4v3r2a4404+_abswk65kjgwrd2n@sdb6lr^3^p' # 9/17剪下至.env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  #真正上線部署時會設定為False 改為False 9/15

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp', #新增的app
    'to_do', #新增於0912
]
#     'mysqlfile', # 2019/09/08 新增mysql
# 9/15新增heroku whitenoise 處理 static 文件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'web_create_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #加上templates路徑
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

WSGI_APPLICATION = 'web_create_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
'''sqlite3'''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
'''09/08 改為 mysql，因為上船雲端，所以db換成 postgresql '''
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'djangomysql',  # 使用數據庫名字 數據需先手動創建
#         'USER':'b10130402',
#         'PASSWORD':'hjkl4660',
#         'HOST':'localhost',  # 指定mysql數據庫所在ip位址'127.0.0.1'
#         'PORT':'3306',
#         'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
#     }
# }
"""9/19 更該為postgresql"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql.psycopg2',
    }
}
### 其 url 24hrs 會更換 ，使用此式 local & heroku 資料庫共通
DATABASES['default'] = dj_database_url.config(default="postgres://dmpdzkbcivfuhy:b2c275dfba4397ed9159d74d22e3727ad122bddc95937cbe6e9560dd4d5dcc68@ec2-174-129-227-128.compute-1.amazonaws.com:5432/da29d5835f52dv")
db_from_env = dj_database_url.config(conn_max_age= 600)
DATABASES['default'].update(db_from_env)
"""9/19 更該為postgresql"""
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hant' #使用中文

TIME_ZONE = 'Asia/Taipei' #使用時區

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ #加入static路徑
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 9/17 新增
django_heroku.settings(locals())