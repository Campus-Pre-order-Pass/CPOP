# models
from Order.models import Order, OrderItem
from Customer.models import Customer
from Shop.models import Vendor, DayOfWeek

# serializers
from Order.serializers import OrderSerializer
from rest_framework import serializers

from Order.OrderLogic.setting import SettingsManager


from datetime import datetime
import pytz
from django.utils import timezone


class OrderVaild():
    @staticmethod
    def validate_order_models(order_instance: Order):
        "檢查 order 格式是否正確"

        try:
            # Validate the order instance using the OrderSerializer
            order_serializer = OrderSerializer(
                data=OrderSerializer(order_instance).data)

            if not order_serializer.is_valid():
                print(order_serializer.errors)
            # raise serializers.ValidationError(order_serializer.errors)

            return order_instance

        except serializers.ValidationError as e:
            # print(e)

            return False

    @staticmethod
    def is_order_valid():
        """
        检查订单对象是否有效
        """

        return True

    @staticmethod
    def check_business_hours(vendor: Vendor, test: bool = False) -> bool:
        """  
            1. 实现检查營業時間的逻辑
            2. 如果營業時間符合要求，返回 True；否则引发异常
        """
        if test:
            return True

        now_time_taipei = datetime.now(pytz.timezone('Asia/Taipei')).time()

        d = DayOfWeek.objects.get(
            vendor_id=vendor.id, day=datetime.now().isoweekday())

        open_time = d.open_time
        close_time = d.close_time

        if not (open_time <= now_time_taipei <= close_time):
            raise ValueError(
                "Current time is outside the open and close time range.")

        return True

    @staticmethod
    def check_inventory(order_item: any, test: bool = False) -> bool:
        """      
            1. 实现檢查庫存的逻辑
            2. 如果庫存足夠，返回 True；否则返回 False
        """

        if test:
            return True

        # TODO: 商家現在沒有要做這個！！！！

        return True

    @staticmethod
    def check_user_purchase_limit(customer: Customer, test: bool = False) -> bool:
        """ 
            1. 实现檢查使用者是否達到購買次數的逻辑
            2. 如果達到購買次數限制，返回 True；否则返回 False
        """

        # Count the number of orders created today
        order_count_today = Order.objects.filter(
            customer=customer, created_at=timezone.now().date()).count()

        # 判斷
        if order_count_today > SettingsManager.MAX_USER_PURCHASE_LIMIT:
            raise ValueError("Exceeded the maximum user purchase limit.")

        return True

    @staticmethod
    def is_special_day(vendor: Vendor, test: bool = False):
        """ 判斷是否是特別，像是六日校慶等等"""
        pass

    @staticmethod
    def is_confirmation_hash_same(vendor: Vendor, test: bool = False):
        pass
