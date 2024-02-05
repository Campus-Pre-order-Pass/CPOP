from Order.core.abstract.printer import PrinterABC
from Order.serializers import OrderRequestBodySerializer
from Order.models import *
from Order.core.module.data_manager import DataManager

from Printer.main import OrderInvoiceGenerator

class Printer(PrinterABC):
    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', False)
        self.order = None
        self.order_items = None
    
        self.data_manager = DataManager(self.test, *args, **kwargs)

    def is_valid(self) -> bool:
        """先判斷是否資料格式正確，需要做`raise報錯`

        Returns:
            bool: _description_
        """
        return True

    def is_connected(self, order: Order, order_items: OrderItem) -> bool:
        """先判斷是否印單機有連線,需要做`raise報錯`
        
        ping...特定 port
        
        """
        return True

    def print(self) -> bool:
        invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        success = invoice_generator.generate_invoice(shop="A", order_details=Order, print_invoice=True, show_invoice=False)
        return success
