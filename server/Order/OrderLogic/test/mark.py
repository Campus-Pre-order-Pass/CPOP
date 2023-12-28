# models
import json
from Order.models import Order, OrderItem
from MenuItem.models import ExtraOption, MenuItem, RequiredOption
from Shop.models import Vendor
from Customer.models import Customer

# serializers
from Order.serializers import OrderSerializer

# tools
from Order.OrderLogic.hash.hash import HashTool
from Order.OrderLogic.vaild.vaild import OrderVaild

#
from faker import Faker
from datetime import datetime

# django
import django
from django.utils import timezone


faker = Faker('zh_TW')


class MarkData():
    extra_option_ids = [1, 2]
    required_option_ids = [1, 2]

    @staticmethod
    def get_data():
        """獲取測試資料"""
        # Initialize Django
        django.setup()

        # Create test data using Faker
        vendor = Vendor.objects.get(id=1)
        customer = Customer.objects.get(id=1)
        menu_item_1 = MenuItem.objects.get(id=1)

        # Get ExtraOption instances based on provided ids
        extra_options = ExtraOption.objects.filter(
            id__in=MarkData.extra_option_ids)

        # Get RequiredOption instances based on provided ids
        required_options = RequiredOption.objects.filter(
            id__in=MarkData.required_option_ids)

        # Create OrderItem and associate ExtraOptions and RequiredOptions using set()
        order_item_1 = OrderItem.objects.create(
            menuItem=menu_item_1,
            quantity=faker.random_int(min=1, max=5),
        )
        order_item_1.extra_option.set(extra_options)

        order_item_1.required_option.set(required_options)

        total_amount = faker.random_number(digits=3)
        order_status = "pending"

        order = Order.objects.create(
            vendor=vendor,
            customer=customer,
            order_time=timezone.now(),
            take_time=timezone.now(),
            total_amount=total_amount,
            order_status=order_status,
            confirmation_hash=HashTool.generate_confirmation_hash()
        )

        order.order_items.add(order_item_1, order_item_1,
                              order_item_1, order_item_1)

        return OrderVaild.validate_order_models(order_instance=order)

    @staticmethod
    def get_json_order_data():
        with open('Order/OrderLogic/test/data.json', 'r') as file:
            python_object = json.load(file)

        # 打印从文件读取并解析得到的 Python 对象
        # print(python_object)

        return python_object
