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
