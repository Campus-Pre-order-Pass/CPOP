from django.test import TestCase


from Printer.main import OrderInvoiceGenerator

from Order.OrderLogic.order_logic import OrderLogic


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
    OrderLogic.test_order()
