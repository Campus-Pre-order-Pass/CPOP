import logging
from pathlib import Path
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


class OrderModelTest(TestCase):
    order_details_example = [
        ["時間: ", "11-05 10:30", ""],
        ["平台: ", "888", ""],
        ["總金額: ", "1000", ""],
        ["波士頓龍蝦蛋餅", "1", ""],
        ["雙色吐司", "1", "巧克力/奶酥"],
        ["紅茶", "1", "去冰"]
    ]

    def test_printer(self):
        # Assuming OrderInvoiceGenerator is in your_module
        # invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        result = invoice_generator.generate_invoice(
            shop="A", order_details=self.order_details_example, print_invoice=True, show_invoice=False)
        # Assert that the result is as expected
        # You may need to adjust this based on the actual return value
        self.assertTrue(result)

        # You can add more assertions based on the expected behavior of your generate_invoice method


class TestAPIView(TestAPIBaseCaseV2):
    def test_PayOrderAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL
        customer_id = 1
        url = reverse("Order:pay_order", args=[customer_id])

        # 发起 GET 请求
        response = client.get(
            url, content_type="application/json", format="json")

        # print(response.content)

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    def test_post_PayOrder(self):
        test_data = MarkData.get_json_order_data()
        url = reverse("Order:pay_order")
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

        # print(response.content)

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)


class OrderLoggerTestCase(TestCase):
    def test_write(self):
        # 获取名为 'order' 的 logger
        logger = logging.getLogger('order')

        # 在此之后，你可以记录不同级别的日志消息
        logger.info('This is a debug message for the order logger.')
