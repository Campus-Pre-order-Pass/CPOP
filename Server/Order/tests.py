from contextlib import AbstractContextManager
import logging
from pathlib import Path
from typing import Any
from django.test import TestCase, override_settings
from django.core.management import call_command

import time

from django.test import Client
from django.urls import reverse
from unittest.mock import MagicMock

from Printer.main import OrderInvoiceGenerator

from Order.OrderLogic.order_logic import OrderLogic
from Order.OrderLogic.test.mark import MarkData
from Order.views import PayOrderAPIView

# TestAPIBaseCase
from helper.base.base_test_case import TestAPIBaseCase, TestAPIBaseCaseV2


from Order.core.trading_system import TradingSystem
from Order.core.module.module import *


class ModuleTestCase(TestCase):
    def test_class(self):
        a = TradingSystem(test=True)
        print(a.test)


class TestAPIView(TestAPIBaseCaseV2):
    def test_PayOrderAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL
        url = reverse("Order:pay_order", kwargs={'uid': "test"})

        # 发起 GET 请求
        response = client.get(
            url, content_type="application/json", format="json")

        # print(response.content)
        TestAPIBaseCaseV2.is_available(response)

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    def test_post_PayOrder(self):
        test_data = MarkData.get_json_order_data()
        url = reverse("Order:pay_order", kwargs={'uid': "test"})
        # url = "v0/api/o/pay"

        # Make a POST request to the view with the test data
        response = self.client.post(url, data=test_data,
                                    format="json")

        TestAPIBaseCaseV2.is_available(response, 201)

        self.assertEqual(response.status_code, 201)

    def test_OrderAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL，并传递参数
        order_id = 4
        url = reverse("Order:order_status", args=[order_id])

        # 发起 GET 请求
        response = client.get(url, content_type="application/json")

        TestAPIBaseCaseV2.is_available(response, 200)

        # print(response.content)

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)


class OrderLoggerTestCase(TestCase):
    def test_write(self):
        # 获取名为 'order' 的 logger
        logger = logging.getLogger('order')

        # 在此之后，你可以记录不同级别的日志消息
        logger.info('This is a debug message for the order logger.')
