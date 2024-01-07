# generate settings
from .settings import *
#     command: python manage.py runserver 0.0.0.0:8000 --settings=Backend.settings_prod

DEBUG = True

# Django Redis 快取配置
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # TODO: 需要改
        "LOCATION": "redis://redis:6379/1",  # 主机名为服务名 "redis"
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
