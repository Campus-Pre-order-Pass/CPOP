from pathlib import Path
from django.test import TestCase, override_settings
from django.core.management import call_command
from rest_framework.test import APITestCase

import time

from django.test import Client
from django.urls import reverse
from unittest.mock import MagicMock


class TestAPIBaseCase(TestCase):
    """在setup 加入測試資料"""
    # @override_settings(DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}})

    def setUp(self):
        super().setUp()
        # 在测试数据库中加载测试数据
        # call_command('flush', interactive=False)  # 非交互式模式，不需要确认
        call_command('loaddata', 'static/json/Shop.json')
        call_command('loaddata', 'static/json/Customer.json')
        call_command('loaddata', 'static/json/MenuItem.json')
        call_command('loaddata', 'static/json/Order.json')


class TestAPIBaseCaseV2(APITestCase):
    """V2 extended APITestCase with support for `slef.client.get(...) methods`"""

    # @override_settings(DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}})
    def setUp(self):
        super().setUp()
        # 在测试数据库中加载测试数据
        # call_command('flush', interactive=False)  # 非交互式模式，不需要确认
        call_command('loaddata', 'static/json/Shop.json')
        call_command('loaddata', 'static/json/Customer.json')
        call_command('loaddata', 'static/json/MenuItem.json')
        call_command('loaddata', 'static/json/Order.json')

    @staticmethod
    def is_available(response, status_code=200):
        if response.status_code != status_code:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))
