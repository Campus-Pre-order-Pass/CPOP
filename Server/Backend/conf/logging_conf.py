import logging
from logging.handlers import RotatingFileHandler


# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/debug.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/info.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'warning_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/warning.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/error.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',
        },
        'critical_file': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/critical.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',

        },

        'order_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/order.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',

        },

        # tasks file

        'tasks_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/tasks.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',

        },


        'printer_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/printer.log',
            'maxBytes': 5*1024*1024,
            'backupCount': 3,
            'formatter': 'verbose',

        },



        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['tasks_file', 'order_file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },

        # 'django': {
        #     'handlers': ['debug_file', 'info_file', 'warning_file', 'error_file', 'critical_file', 'tasks_file', 'order_file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
        # 添加一个新的Logger来处理测试模式下的日志
        # 'test_logger': {
        #     'handlers': ['console'],  # 使用控制台处理程序
        #     'level': 'DEBUG',  # 设置日志级别
        #     'propagate': False,
        # },
        # 'celery': {
        #     'handlers': ['console', 'tasks_file'],
        #     'level': 'DEBUG',
        # },

        # 'tasks': {
        #     'handlers': ['tasks_file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },

        'order': {
            'handlers': ['order_file'],
            'level': 'INFO',
            'propagate': True,
        },

    },
}


LOG_VIEWER_FILES = ['django.log', 'job.log']
LOG_VIEWER_FILES_PATTERN = '*.log*'
LOG_VIEWER_FILES_DIR = 'logs/'
LOG_VIEWER_PAGE_LENGTH = 25       # total log lines per-page
LOG_VIEWER_MAX_READ_LINES = 1000  # total log lines will be read
# Max log files loaded in Datatable per page
LOG_VIEWER_FILE_LIST_MAX_ITEMS_PER_PAGE = 25
LOG_VIEWER_PATTERNS = ['[INFO]', '[DEBUG]',
                       '[WARNING]', '[ERROR]', '[CRITICAL]']
# String regex expression to exclude the log from line
LOG_VIEWER_EXCLUDE_TEXT_PATTERN = None

# Optionally you can set the next variables in order to customize the admin:
LOG_VIEWER_FILE_LIST_TITLE = "Custom title"
LOG_VIEWER_FILE_LIST_STYLES = "/static/css/logs_css.css"
