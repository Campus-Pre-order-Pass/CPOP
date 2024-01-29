from Order.core.abstract.printer import PrinterABC
from Order.serializers import OrderRequestBodySerializer
from Order.models import *
from Order.core.module.data_manager import DataManager


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

    def print(self) -> bool:
        """_summary_
        """
        # Your print logic here
        return True
