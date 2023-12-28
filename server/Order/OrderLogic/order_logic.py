"""交易系統的邏輯"""

import hashlib
import secrets
from django.utils import timezone

# SettingsManager
from Order.OrderLogic.setting import SettingsManager

# ModelRetriever
from Order.OrderLogic.helper.get_models import ModelManager

# OrderVaild
from Order.OrderLogic.vaild.vaild import OrderVaild

# Helper
from Order.OrderLogic.helper.helper import Helper

# models
from ..models import Order, OrderItem
from Shop.models import Vendor
from Customer.models import Customer

# hash
from Order.OrderLogic.hash.hash import HashTool

# mark
from Order.OrderLogic.test.mark import MarkData


class OrderLogic:
    """
    1. 檢查 ordering

    2. 創建 ordering

    3. 建立 ordering

    """

    TEST = False

    V = "0"

    # _instance = None  # 類變量，用於保存實例

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         # 如果實例還不存在，則創建一個新的實例
    #         cls._instance = super().__new__(cls)
    #         # 在這裡進行初始化/配置
    #         cls._instance.config = cls._load_config()
    #     return cls._instance

    def check_order(self, data: any) -> any:
        vendor_id = data.get('vendor_id')
        customer_id = data.get('customer_id')
        menu_items = data.get('order_items')

        # 检查是否成功获取到必要的键值，如果没有，引发异常
        if vendor_id is None or customer_id is None or menu_items is None:
            raise ValueError(
                "Failed to retrieve necessary key-value pairs from data.", SettingsManager.FORMAT_ERROR)

        vendor = ModelManager.creat_model_instance(Vendor, vendor_id)
        customer = ModelManager.creat_model_instance(Customer, customer_id)
        order_items = ModelManager.create_order_items(menu_items)

        data = {
            "vendor": vendor,
            "customer": customer,
            "order_items": order_items
        }

        return data

    def create_order(self, data: any) -> Order:
        """交易創建"""

        # 解構
        vednor = data["vendor"]
        customer = data["customer"]
        order_items = data["order_items"]

        try:
            OrderVaild.is_order_valid()
        except Exception as e:
            raise ValueError(e, SettingsManager.ERROR_CODE)
        try:
            # 檢查使用者購買上限
            OrderVaild.check_user_purchase_limit(
                customer=customer, test=self.TEST)
        except Exception as e:
            raise ValueError(e, SettingsManager.USER_PURCHASE_LIMIT_ERROR)
        try:
            # 減持是否在營業時間
            OrderVaild.check_business_hours(vendor=vednor, test=self.TEST)
        except Exception as e:
            raise ValueError(e, SettingsManager.BUSINESS_HOURS_ERROR)
        try:
            # 实现檢查庫存的逻辑
            for order_item in order_items:
                OrderVaild.check_inventory(
                    order_item=order_item, test=self.TEST)
        except Exception as e:
            raise ValueError(e, SettingsManager.INVENTORY_ERROR)

        # finally:
        #     print("Order")

        order_table = Order.objects.create(
            vendor=vednor,
            customer=customer,
            order_time=timezone.now(),
            take_time=timezone.now(),
            total_amount=Helper.get_total_amount(order_items=order_items),
            order_status="pending",
        )

        for order_item in order_items:
            order_table.order_items.add(order_item)

        # 加入hash算法
        order_table.confirmation_hash = HashTool.hash_data(data=order_table)

        return order_table

    def order(self, order: Order) -> str:

        return "hash code"

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
