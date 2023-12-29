from django.test import TestCase
import time

from django.test import Client
from django.urls import reverse
from unittest.mock import MagicMock

from Printer.main import OrderInvoiceGenerator

from Order.OrderLogic.order_logic import OrderLogic
from Order.OrderLogic.test.mark import MarkData
from Order.views import PayOrderAPIView


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


class OrderPayTest(TestCase):
    # ./manage.py test Order.tests.OrderPayTest

    # start_time = time.time()

    # # 执行你的代码
    # order_s = OrderLogic()
    # order_s.setTest(True)
    # json_data = order_s.test_order()

    # # check
    # order_s.check_order(data=json_data)

    # # 交易
    # order_s.order()

    # orders = order_s.get_order_table()

    # print(orders.show())

    # # 记录结束时间
    # end_time = time.time()

    # # 计算执行时间
    # execution_time = end_time - start_time
    # print(f"Total execution time: {execution_time} seconds")
    def test_get_json_order_results(self):
        data = MarkData.get_json_order_results()
        print(data)


class TestPayOrderAPIView(TestCase):
    # def setUp(self):
    #     # 在这里执行测试数据库的初始化工作
    #     # 这可能包括数据库迁移、创建模型实例等
    #     call_command('migrate')
    #     # 其他初始化工作

    # def tearDown(self):
    #     # 在这里执行测试数据库的清理工作
    #     # 这可能包括删除测试用例创建的模型实例等
    #     # 通常会使用 `django.test.TestCase` 提供的数据库刷新机制
    #     self._fixture_teardown()

    # def test_pay_order_success(self):
    # Mock the necessary dependencies

    # Create a test client
    client = Client()

    # Prepare test data
    test_data = MarkData.get_json_order_data()

    # Use the reverse function to get the URL for the view
    # Replace "pay-order" with the actual URL name
    url = reverse("Order:pay_order")

    # Make a POST request to the view with the test data
    response = client.post(url, data=test_data,
                           content_type="application/json")
    # 打印响应状态码
    print(f"Status Code: {response.status_code}")

    # 打印响应头
    # print("Response Headers:")
    # for header, value in response.items():
    #     print(f"{header}: {value}")

    # 打印响应内容
    print("Response Content:")
    print(response.content.decode('utf-8'))
    # # Assert the expected behavior

    # expected_response = {
    #     "message": "Order created successfully", "hash_code": "hash_code"}
    # self.assertEqual(response.status_code, 201)
    # self.assertEqual(response.json(), expected_response)
