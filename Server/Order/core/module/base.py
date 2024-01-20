# helpers
from Order.core.helper.vaild import Valid
from Order.core.helper.function import PrinterTool
from Order.core.module.data_manager import DataManager
from Order.core.module.configuration import Configuration
from Order.core.helper.tool import Tool


class BaseClass(object):
    """base class and tools

    Args:
        object (_type_): _description_
    """

    Version = (0, 0, 0)

    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', False)
        self.vaild = Valid()
        self.printer = PrinterTool()
        self.tool = Tool()
        self.configuration = Configuration()

        self.data_manager = DataManager(self.test, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """_call method_
        """
        print(f"參數：{args}, 關鍵字參數：{kwargs}")
