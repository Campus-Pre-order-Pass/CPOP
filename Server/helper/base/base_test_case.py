from pathlib import Path
import sys
from django.test import TestCase, override_settings
from django.core.management import call_command
from rest_framework.test import APITestCase
from io import StringIO

import time

from django.test import Client
from django.urls import reverse
from unittest.mock import MagicMock
from unittest.mock import patch


class TestAPIBaseCase(TestCase):
    """在setup 加入測試資料"""
    # @override_settings(DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}})

    def setUp(self):
        super().setUp()

        # 创建 StringI/O 对象来捕获输出
        self.stdout_captured = StringIO()
        self.stderr_captured = StringIO()

        # 使用 patch 装饰器覆盖 sys.stdout 和 sys.stderr
        with patch('sys.stdout', self.stdout_captured), patch('sys.stderr', self.stderr_captured):
            # 调用管理命令加载测试数据
            call_command('loaddata', 'static/json/Shop.json')
            call_command('loaddata', 'static/json/Customer.json')
            call_command('loaddata', 'static/json/MenuItem.json')
            call_command('loaddata', 'static/json/Order.json')

        # 重置 StringI/O 对象以便后续的断言
        self.stdout_captured = StringIO()
        self.stderr_captured = StringIO()

    def tearDown(self):
        super().tearDown()


class TestAPIBaseCaseV2(APITestCase):
    """V2 extended APITestCase with support for `slef.client.get(...) methods`"""

    def setUp(self):
        super().setUp()

        # 创建 StringI/O 对象来捕获输出
        self.stdout_captured = StringIO()
        self.stderr_captured = StringIO()

        # 使用 patch 装饰器覆盖 sys.stdout 和 sys.stderr
        with patch('sys.stdout', self.stdout_captured), patch('sys.stderr', self.stderr_captured):
            # 调用管理命令加载测试数据
            call_command('loaddata', 'static/json/Shop.json')
            call_command('loaddata', 'static/json/Customer.json')
            call_command('loaddata', 'static/json/MenuItem.json')
            call_command('loaddata', 'static/json/Order.json')

        # 重置 StringI/O 对象以便后续的断言
        self.stdout_captured = StringIO()
        self.stderr_captured = StringIO()

    def tearDown(self):
        super().tearDown()

    @staticmethod
    def is_available(response, status_code=200):
        if response.status_code != status_code:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))
