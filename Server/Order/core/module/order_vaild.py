# models
from Order.models import Order, OrderItem
from Customer.models import Customer
from Order.OrderLogic.error.error import OrderCreationError
from Order.core.module.serializers import OrderRequestBodySerializer
from Shop.models import Vendor, DayOfWeek

# serializers
from Order.serializers import OrderSerializer
from rest_framework import serializers

from Order.OrderLogic.setting import SettingsManager
from Order.core.module.base import BaseClass


from datetime import datetime
import pytz
from django.utils import timezone


class OrderVaild(BaseClass):
    def __init__(self, *args, **kwargs):
        super(OrderVaild, self).__init__(*args, **kwargs)

    def check_daily_purchase_limit(self, order: OrderRequestBodySerializer):

        vendor_id = order.validated_data["vendor_id"]

        c = self.data_manager.get_vendor_conditions(vendor_id)

        # 檢查當天購買人數上限
        if c.max_purchase_count <= c.current_purchase_count:
            raise ValueError("max_purchase_count overflowed !!")

    @staticmethod
    def is_order_valid() -> bool:
        """
        检查订单对象是否有效
        """

        return True

    @staticmethod
    def check_business_hours(vendor_id: int) -> bool:
        """  
            1. 实现检查營業時間的逻辑
            2. 如果營業時間符合要求，返回 True；否则引发异常
        """

        vendor = Vendor.objects.get(id=vendor_id)

        now_time_taipei = datetime.now(pytz.timezone('Asia/Taipei')).time()

        d = DayOfWeek.objects.get(
            vendor_id=vendor.id, day=datetime.now().isoweekday())

        open_time = d.open_time
        close_time = d.close_time

        if not (open_time <= now_time_taipei <= close_time):
            raise ValueError(
                "Current time is outside the open and close time range.")

        return True

    def check_menu_items_inventory(self, item: dict, vendor_id: int) -> bool:
        """      
            1. 实现檢查庫存的逻辑
            2. 如果庫存足夠，返回 True；否则返回 False
        """
        status = self.data_manager.get_menu_items_status_data(
            item.get("menu_item_id"), vendor_id)

        if status.remaining_quantity - 1 < 0:
            raise ValueError(
                f"{status.menu_item} , {status.remaining_quantity} is out of stock")

        return True

    @staticmethod
    def check_user_purchase_limit(customer_id: int, test: bool = False) -> bool:
        """
            1. 实现檢查使用者是否達到購買次數的逻辑
            2. 如果達到購買次數限制，返回 True；否则返回 False
        """

        customer = Customer.objects.get(id=customer_id)

        # Count the number of orders created today
        order_count_today = Order.objects.filter(
            customer=customer, created_at=timezone.now().date()).count()

        # 判斷
        if order_count_today > SettingsManager.MAX_USER_PURCHASE_LIMIT:
            raise ValueError(
                "Exceeded the maximum user purchase limit.")

        return True

    def check_customer_take_time(self, taken_time) -> bool:
        # vendor = Vendor.get_vendor(vendor_id)

        # 获取今天的日期
        today_date = self.tool.get_now_time_taipei()

        # 将 taken_time 转换为日期对象
        taken_date = taken_time.date()

        # 比较 taken_date 是否为今天
        if taken_date != today_date:
            raise ValueError(
                "error take time")

        return True

    @staticmethod
    def is_special_day(vendor: Vendor, test: bool = False):
        """ 判斷是否是特別，像是六日校慶等等"""
        pass

    @staticmethod
    def is_confirmation_hash_same(vendor: Vendor, test: bool = False):
        pass

    @staticmethod
    def is_over_timezone(vendor: Vendor, test: bool = False):
        pass
