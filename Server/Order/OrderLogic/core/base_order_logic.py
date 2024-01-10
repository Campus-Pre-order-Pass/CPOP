

from Order.OrderLogic.vaild.vaild import OrderVaild
from Order.OrderLogic.hash.hash import HashTool
from Order.OrderLogic.helper.tool import Tool
from Order.OrderLogic.helper.get_models import ModelManager
from Order.OrderLogic.test.mark import MarkData


class Base(object):
    def __init__(self, *args, **kwargs):
        self.vaild = OrderVaild()
        self.hash_tools = HashTool()
        self.tool = Tool()
        self.model_manager = ModelManager()
        self.mark = MarkData()

        assert self.hash_tools, "hash_tools init error"
