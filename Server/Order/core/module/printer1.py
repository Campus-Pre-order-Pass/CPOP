from Order.core.abstract.printer import PrinterABC
from Order.serializers import OrderRequestBodySerializer
from Order.models import *
from server.printer import OrderInvoiceGenerator
from Order.core.module.error import BaseError, PrinterError


class Printer(PrinterABC):
    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', False)
        self.order = None
        self.order_items = None

    def is_valid(self) -> bool:
        try:
            # 進行某些操作，可能導致 printer 錯誤
            # ...

            # 如果發生 printer 錯誤，拋出 PrinterError
            raise PrinterError("Printer error message",
                               error_code=456, error_source="specific_printer")
        except PrinterError as e:
            # 處理 printer 錯誤
            print(f"Printer Error: {e}")
            print(f"Error Code: {e.code}")
            print(f"Error Source: {e.error_source}")
        return True

    def is_connected(self, order: Order, order_items: OrderItem) -> bool:
        """先判斷是否印單機有連線,需要做`raise報錯`
        Returns:
            bool: _description_
        """
        self.order = order
        self.order_items = order_items
        # ex 獲取 extra_option
        # for order_item in order_items:
        #     print(order_item.extra_option.all())
        #     print(order_item.required_option.all())
        return True

    def print(self, order: Order) -> bool:
        invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        success = invoice_generator.generate_invoice(
            shop="A", order_details=Order, print_invoice=True, show_invoice=False)
        if not success:
            # 如果 success 的值為 False，拋出一個自訂的錯誤
            raise PrinterError("Failed to generate/print the invoice",
                               error_code=789, error_source="specific_printer")
        return success
