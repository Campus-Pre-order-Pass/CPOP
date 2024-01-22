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

# Django Redis 快取配置
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # TODO: 需要改
        # "LOCATION": "redis://redis:6379/1",  # 主机名为服务名 "redis"
        "LOCATION": "redis://127.0.0.1:6379/1",  # 主机名为服务名 "redis"

        # "LOCATION": "redis://0.0.0.0:6379/1",  # 主机名为服务名 "redis"
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
current_db_name = connections['default'].settings_dict['ENGINE']


PrinterTool.print_info_line()
PrinterTool.print_red("use settings_setting")
PrinterTool.print_green(f"database: {current_db_name}")
PrinterTool.print_green(f"django_redis: {CACHES['default']['LOCATION']}")
