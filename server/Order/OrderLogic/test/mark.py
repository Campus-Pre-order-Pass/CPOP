# models
from Order.models import Order
from Shop.models import Vendor
from Customer.models import Customer

from faker import Faker

# django
import django


class MarkData():
    @staticmethod
    def get_data():
        """獲取測試資料"""
        # wait
        django.setup()

        # test data

        o = Order.objects.create(
            vendor=Vendor.objects.get(id=1),
            customer=Customer.objects.get(id=1)
        )

        return o
