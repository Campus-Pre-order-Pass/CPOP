from Order.core.abstract.printer import PrinterABC
from Order.serializers import OrderRequestBodySerializer


class Printer(PrinterABC):
    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', False)
        self.order = None

    def is_valid(self) -> bool:
        """先判斷是否資料格式正確，需要做`raise報錯`

        Returns:
            bool: _description_
        """
        return True

    def is_connected(self, order: OrderRequestBodySerializer) -> bool:
        """先判斷是否印單機有連線,需要做`raise報錯`

        Returns:
            bool: _description_
        """

        self.order = order
        return True

    def print(self) -> bool:
        """_summary_
        """
        # Your print logic here
        return True
