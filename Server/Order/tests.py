from django.test import TestCase
import time


from Printer.main import OrderInvoiceGenerator

from Order.OrderLogic.order_logic import OrderLogic
from Order.OrderLogic.test.mark import MarkData


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
