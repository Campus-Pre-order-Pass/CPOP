"""交易系統的邏輯"""

import hashlib
import secrets
from django.utils import timezone

# abstract
from Order.OrderLogic.abstract.abstractmethod import AbstractOrderLogic

# SettingsManager
from Order.OrderLogic.setting import SettingsManager

# ModelRetriever
from Order.OrderLogic.helper.get_models import ModelManager

# OrderVaild
from Order.OrderLogic.vaild.vaild import OrderVaild

# Helper
from Order.OrderLogic.helper.helper import Helper

# printer
from Printer.main import OrderInvoiceGenerator

# error
from Order.OrderLogic.error.error import OrderCreationError

# models
from ..models import Order, OrderItem
from Shop.models import Vendor
from Customer.models import Customer

# hash
from Order.OrderLogic.hash.hash import HashTool

# mark
from Order.OrderLogic.test.mark import MarkData


class OrderLogic(AbstractOrderLogic):
    """
    1. 檢查 ordering

    2. 創建 ordering

    3. 建立 ordering

    """

    TEST = False

    V = "0"

    order_table = any

    vendor = any

    customer = any

    order_items = any

    menu_items = any

    # _instance = None  # 類變量，用於保存實例

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         # 如果實例還不存在，則創建一個新的實例
    #         cls._instance = super().__new__(cls)
    #         # 在這裡進行初始化/配置
    #         cls._instance.config = cls._load_config()
    #     return cls._instance

    def __str__(self) -> str:
        super().__str__()
        return self.order

    def check_order(self, data: any) -> bool:
        """檢查 order"""
        vendor_id = data.get('vendor_id')
        customer_id = data.get('customer_id')
        order_items = data.get('order_items')

        self.order_items = order_items

        # if self.TEST:
        #     print(vendor_id, customer_id, menu_items)

        # 检查是否成功获取到必要的键值，如果没有，引发异常
        if vendor_id is None or customer_id is None or order_items is None:
            raise OrderCreationError(
                "Failed to retrieve necessary key-value pairs from data.",
                SettingsManager.FORMAT_ERROR,
                f"{self.__class__.__name__}.check_order")

        self.vendor = ModelManager.creat_model_instance(Vendor, vendor_id)
        self.customer = ModelManager.creat_model_instance(
            Customer, customer_id)
        #  order_items = ModelManager.create_order_items(menu_items)

        # self.order_items = order_items

        # 判斷事件

        try:
            OrderVaild.is_order_valid()
        except Exception as e:
            raise OrderCreationError(
                e, SettingsManager.ERROR_CODE, f"{self.__class__.__name__}.check_order")
        try:
            # 檢查使用者購買上限
            OrderVaild.check_user_purchase_limit(
                customer=self.customer, test=self.TEST)
        except Exception as e:
            raise OrderCreationError(
                e, SettingsManager.USER_PURCHASE_LIMIT_ERROR, f"{self.__class__.__name__}.check_order")
        try:
            # 檢查是否在營業時間
            OrderVaild.check_business_hours(vendor=self.vendor, test=self.TEST)
        except Exception as e:
            raise OrderCreationError(
                e, SettingsManager.BUSINESS_HOURS_ERROR,  f"{self.__class__.__name__}.check_order")
        try:
            # 实现檢查庫存的逻辑
            for order_item in self.order_items:
                OrderVaild.check_inventory(
                    order_item=self.order_items, test=self.TEST)
        except Exception as e:
            raise OrderCreationError(
                e, SettingsManager.INVENTORY_ERROR, f"{self.__class__.__name__}.check_order")

        # finally:
        #     print("Order")

        return True

    def create_order(self):
        pass

    def order(self) -> str:
        """交易"""
        order_table = Order(
            vendor=self.vendor,
            customer=self.customer,
            order_time=timezone.now(),
            take_time=timezone.now(),
            order_status="created",
        )

        # 加入hash算法
        order_table.confirmation_hash = HashTool.hash_data(data=order_table)

        order_table.order_status = "processing"
        order_table.save()

        # TODO: 要改
        self.order_table = order_table

        ModelManager.create_order_items(
            self.order_items, self.order_table)

        # 給 printer
        # try:
        #     invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
        #     result = invoice_generator.generate_invoice(
        #         shop="A", order_details=self.order_details_example, print_invoice=True, show_invoice=False)

        #     order_table.order_status = "processing"
        #     order_table.save()
        # except Exception as e:
        #     raise OrderCreationError(str(e), SettingsManager.PRINTER_ERROR)

        return self.order_table.confirmation_hash

    def cancel_order(self, data) -> str:
        pass

    def get_order_list(order_id: int) -> Order:
        # 处理获取订单列表的逻辑，例如从数据库中获取订单数据
        # 这里只是一个示例，你需要根据实际情况来编写具体的逻辑
        pass

    def save_order_log(self) -> bool:
        pass

    def test_order(self):
        try:
            # data = MarkData.get_data()
            data = MarkData.get_json_order_data()
            return data
        except Exception as e:
            # print(e)
            return False

    def setTest(self, test: bool) -> bool:
        self.TEST = test

        return self.TEST

    def get_order_table(self) -> Order:
        return self.order_table
