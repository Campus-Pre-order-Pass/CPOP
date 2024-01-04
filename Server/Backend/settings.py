"""
Django settings for Backend project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import socket
import sentry_sdk
import os
from pathlib import Path
import sys
from decouple import config
from django.core.management.utils import get_random_secret_key


# INSTALLED_APPS =================================================
from Backend.conf.install_app import INSTALLED_APPS


# DATABASES
from Backend.conf.db_conf import DATABASES

# LOGGING =================================================
from Backend.conf.logging_conf import LOGGING

# JAZZMIN_SETTINGS =================================================
from Backend.conf.jazzmin_conf import JAZZMIN_SETTINGS


# SWAGGER_SETTINGS =================================================
from Backend.conf.swagger_conf import SWAGGER_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k=^(!mg80*&)4$cbw8whm!q0%62%n3#w%p#ox5o_k08il&1m@2'

"""
name:  hungwei  
pas:   Ws7tscypC2VrpQpwbsQdURUe97nuRF3p
"""

# SECURITY WARNING: don't run with debug turned on in production!


config.encodeing = 'utf-8'

# SECRET_KEY = config('SECRET_KEY')
# SECRET_KEY = get_random_secret_key()

# DEBUG = config('DEBUG', default=False, cast=bool)

# test
DEBUG = True
TEST = True


ALLOWED_HOSTS = ['*', ]

# ssl support/
# SECURE_SSL_REDIRECT = config(
#     'SECURE_SSL_REDIRECT', default=False, cast=bool)

SECURE_SSL_REDIRECT = False
# Application definition


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://0.0.0.0:3000',
    'http://0.0.0.0:3001',
    'http://0.0.0.0:3002',
    # site
    # 'https://cpop.iside.shop',
    # api and admin sites
    'https://cpop.api.iside.shop',
]


CSRF_TRUSTED_ORIGINS = [
    # 'https://cpop.iside.shop',
    'https://cpop.api.iside.shop',
    'http://127.0.0.1',
]


INTERNAL_IPS = [
    '127.0.0.1'
]


# axes
if DEBUG:
    # 如果你在本地使用 DEBUG 模式，请禁用 django-axes
    AXES_ENABLED = False

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# 暫時不要寫權限
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

MIDDLEWARE = [

    # axes
    # 'axes.middleware.AxesMiddleware',
    # cache
    'django.middleware.common.CommonMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    # application
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # core
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',


    # DebugToolbarMiddleware
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # SecurityMiddleware
    # 'djangosecure.middleware.SecurityMiddleware',





    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'Backend.urls'

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

WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# TODO: 需要改
# USE_DEFAULT_DB = !DEBUG


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True
# 禁用时区支持

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# TODO: 需要改
STATIC_ROOT = '/Users/hungwei/Desktop/CPOP/CPOP/static/'


MEDIA_URL = '/media/'

# TODO: 需要改

# MEDIA_ROOT = '/Users/hungwei/Desktop/CPOP/CPOP/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RATELIMITS = {
    'defult': '100/m',
    # track
    'track': "100/m",
    # task
    'task': "10/m",
    # user
    'user': '20/m',
    # admin url
    "admin": '10/m',
    'img': '100/m',
    # comment
    'comment': '5/m',
}

RATELIMITS_DEFAULT = "100/m"
RATELIMITS_ADMIN = "10/m"
RATELIMITS_USER = "10/m"
RATELIMITS_IMAGE = "20/m"
RATELIMITS_TRACK = "20/m"


# 使用django-apscheduler作为APScheduler的后端
SCHEDULER_JOBSTORES = {
    'default': {
        'type': 'django_apscheduler.jobstores:DjangoJobStore'
    }
}

# Format string for displaying run time timestamps in the Django admin site. The default
# just adds seconds to the standard Django format, which is useful for displaying the timestamps
# for jobs that are scheduled to run on intervals of less than one minute.
#
# See https://docs.djangoproject.com/en/dev/ref/settings/#datetime-format for format string
# syntax details.
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# Maximum run time allowed for jobs that are triggered manually via the Django admin site, which
# prevents admin site HTTP requests from timing out.
#
# Longer running jobs should probably be handed over to a background task processing library
# that supports multiple background worker processes instead (e.g. Dramatiq, Celery, Django-RQ,
# etc. See: https://djangopackages.org/grids/g/workers-queues-tasks/ for popular options).
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'translations'),  # 将 'translations' 更改为您的翻译文件所在的目录
]


# logger =================================================================


# email ================================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# SMTP服务器和端口
EMAIL_HOST = 'smtp-relay.brevo.com'
EMAIL_PORT = 587

# 使用TLS加密
EMAIL_USE_TLS = False

# 发件人邮箱地址和密码（Gmail账户）
EMAIL_HOST_USER = 'iserver2023@gmail.com'
EMAIL_HOST_PASSWORD = 'S3h6aQ8U1Tf0zdC9'

# email detail
COMP = "其他聯絡人: 賴泓瑋 lai09150915@gmail.com"
ADMIN_DNS = "https://sql.iside.shop/"
SUBJECT = "iriver 系統通知"

# admin
ADMIN_URL = "http://127.0.0.1:5002"

ADMIN_ACCOUNT = "4PBvQRaKaZHR2dSNvTv8r664yS7etm6NtK6AsZ39mYzQQsQbaAr6PAfVpXM52sQ6"
ADMIN_PASSWORD = "PM43qE35fNAntftDA95b5N5ysnDD2wfabTwMyTbxqczt3pHYHDM7SsXFS4wb5XNY"


# constants

CAMPUS_CHOICES = [
    ('建功校區', '建功校區'),
    ('第一校區', '第一校區'),
    ('燕巢校區', '燕巢校區'),
]

# admin
SITEHEADER = 'CPOP後台管理'


# Django Redis 快取配置
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # TODO: 需要改
        # "LOCATION": "redis://redis:6379/1",  # 主机名为服务名 "redis"
        "LOCATION": "redis://0.0.0.0:6379/1",  # 主机名为服务名 "redis"
        "OPTIONS": {
            "SOCKET_CONNECT_TIMEOUT": 5,  # 連接超時（秒為單位）
            "SOCKET_TIMEOUT": 5,  # Socket 超時（秒為單位）
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",  # 使用 Zlib 壓縮機制
            "IGNORE_EXCEPTIONS": True,  # 忽略快取例外
            # redis客户端类
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }
    }
}


# 日誌忽略例外
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

"""
CACHE_MIDDLEWARE_ALIAS：用于存储的缓存别名
CACHE_MIDDLEWARE_SECONDS：每个页面应缓存的秒数
CACHE_MIDDLEWARE_KEY_PREFIX：用于生成缓存
"""
CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 300  # 5 分鐘的示例
# TODO: need to change cache timeout
CACHE_MIDDLEWARE_SECONDS = 0  # 5 分鐘的示例
CACHE_MIDDLEWARE_KEY_PREFIX = "cache_redis_demo_first"


# 配置session的引擎为cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 此处别名依赖缓存的设置
SESSION_CACHE_ALIAS = 'default'


# 定義不同情況下的快取時間（秒為單位）

CACHE_TIMEOUT_SHORT = 60 * 5  # 5 分鐘
CACHE_TIMEOUT_LONG = 60 * 60  # 1 小時


# django-axes
# 進用
AXES_ENABLED = config(
    'AXES_ENABLED', default=False, cast=bool)

AXES_FAILURE_LIMIT = 20  # 允许失败尝试的最大次数
AXES_COOLOFF_TIME = 60  # 封锁用户的时间（分钟），在此时间内用户将无法登录
AXES_LOCKOUT_TEMPLATE = 'axes/lockout.html'  # 封锁时显示的模板
# AXES_USE_USER_AGENT = True  # 是否使用用户代理信息进行封锁
AXES_LOCKOUT_BY_COMBINATION = True  # 是否使用 IP 和用户代理的组合进行封锁


# csp

CSP = {
    'default-src': "'self'",
    'script-src': ["'self'", 'https://cpop.iside.shop'],
    'style-src': ["'self'", 'https://cpop.iside.shop'],
}


# CSP = {
#     'default-src': "'self'",
#     'script-src': ["'self'"],
#     'style-src': ["'self'"],
# }
CSP_REPORT_ONLY = config('CSP_REPORT_ONLY', default=False, cast=bool)
CSP_REPORT_URI = '/csp-report-endpoint/'

# sentry_sdk


# sentry_sdk.init(
#     dsn="https://1dc3016976dc850d2a3db9674b970f9c@o4506253256491008.ingest.sentry.io/4506253257998336",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )


# Q_CLUSTER = {
#     'name': 'django_q',
#     'workers': 8,
#     'recycle': 500,
#     'timeout': 60,
#     'compress': True,
#     'save_limit': 250,
#     'queue_limit': 500,
#     'cpu_affinity': 1,
#     'label': '排程管理',
#     'redis': {
#         'host': '127.0.0.1',
#         'port': 6379,
#         'db': 0, }
# }
# 获取主机名

ANALYTICAL_INTERNAL_IPS = ['127.0.0.1']  # 用于本地开发
ANALYTICAL_AUTO_IDENTIFY = True

ANALYTICAL_PROVIDERS = {
    'ga4': {
        'GOOGLE_ANALYTICS_MEASUREMENT_ID': 'Your-GA4-Measurement-ID',
    },
}


# 版本
V = "v0"
