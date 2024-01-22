#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# check
from helper.script.check_redis import Check


# if sys.version_info >= (3, 9):
#     import select

# if sys.version_info < (3, 4):
#     raise RuntimeError('This application must be run under Python 3.4 '
#                        'or later.')

test = False


def main():
    """Run administrative tasks."""
    # TODO: change this to
    if test:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Backend.settings_test')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Backend.settings_dev')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Backend.settings_prod')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# 在这里执行初始化和检查
Check.init_sql()
# Check.check_redis()

if __name__ == '__main__':
    main()
