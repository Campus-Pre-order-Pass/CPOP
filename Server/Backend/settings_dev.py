# django
from django.db import connections
# tools
from helper.tool.function import PrinterTool
# generate settings
from .settings import *

DATABASES = {
    # sqlite3

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    # postgresql
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'postgres',      # 你的数据库名称
    #     'USER': 'myuser',          # 你的数据库用户名
    #     'PASSWORD': 'mypassword',  # 你的数据库密码
    #     'HOST': 'localhost',       # 数据库服务器的主机名，如果在本地运行，通常是 'localhost'
    #     'PORT': '5432',            # 数据库服务器的端口，默认是 5432
    # }
}

# dev 模式
CACHE_MIDDLEWARE_SECONDS = 0  # 5 分鐘的示例

# 获取当前数据库配置的名称
current_db_name = connections['default'].settings_dict['ENGINE']


PrinterTool.print_green(f"use db {current_db_name}")


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
