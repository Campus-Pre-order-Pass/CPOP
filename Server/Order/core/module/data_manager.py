

# models
import json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, QuerySet
from rest_framework.exceptions import ValidationError

# models
from MenuItem.models import *
from Order.models import *
from Shop.models import *

from Order.OrderLogic.error.error import *

# Configuration
from Order.core.module.configuration import Configuration
from Order.core.helper.tool import Tool

# mdoels
from Shop.models import *
from Shop.serializers import *
from Order.core.module.serializers import *


class DataManager():
    def __init__(self, test: bool = False, *args, **kwargs):
        self.test = test
        self.vednor = None
        self.customer = None

    def creat_model_instance(self, model_class: Model, id: int) -> QuerySet:
        try:
            # 使用 objects.get() 获取模型实例
            return model_class.objects.get(id=id)
        except ObjectDoesNotExist:
            raise OrderCreationError(
                f"{model_class.__name__} not found for the given id.", code=Configuration.MODELS_NOT_FOUND)
        except Exception as e:
            # 捕捉其他可能的异常
            raise OrderCreationError(
                f"An error occurred while retrieving {model_class.__name__}: {str(e)}", code=Configuration.MODELS_ERROR)

    def create_order_items(self, order_items: any, order: Order) -> any:
        created_order_items = []

        for order_item_data in order_items:
            menu_item_id = order_item_data.get('menu_item_id')
            extra_option_ids = order_item_data.get('extra_option_ids', [])
            required_option_ids = order_item_data.get(
                'required_option_ids', [])
            quantity = order_item_data.get('quantity')

            # Get ExtraOption instances based on provided ids
            extra_options = ExtraOption.objects.filter(
                id__in=extra_option_ids)

            # Get RequiredOption instances based on provided ids
            required_options = RequiredOption.objects.filter(
                id__in=required_option_ids)

            # Create OrderItem instance
            order_item_instance = OrderItem.objects.create(
                order=order,
                menuItem=self.creat_model_instance(
                    model_class=MenuItem, id=menu_item_id),
                quantity=quantity
            )

            # Add ExtraOption and RequiredOption instances to OrderItem
            order_item_instance.extra_option.set(extra_options)
            order_item_instance.required_option.set(required_options)

            # Append the created OrderItem instance to the list
            created_order_items.append(order_item_instance)

        return created_order_items

    @staticmethod
    def get_json_order_data() -> dict:
        with open('Order/core/mock/data.json', 'r') as file:
            python_object = json.load(file)

        # 打印从文件读取并解析得到的 Python 对象
        # print(python_object)

        return python_object

    @staticmethod
    def get_json_order_results() -> any:
        with open('Order/core/mock/response.json', 'r') as file:
            python_object = json.load(file)

        # 打印从文件读取并解析得到的 Python 对象
        # print(python_object)

        return python_object

    def get_vendor_conditions(self, vendor_id: int):

        if self.test:
            return VendorDailyMetrics.generate_fake_vendor_daily_metrics(vendor_id=vendor_id)
        try:
            return VendorDailyMetrics.get_today_status(vendor_id=vendor_id)
        except Vendor.DoesNotExist:
            raise VendorConditionSerializerError(
                f"Vendor with id {vendor_id} does not exist",
                Configuration.MODELS_ERROR,
                f"VendorConditionSerializerError.{__class__.__name__}"
            )
        except ValidationError as e:
            raise VendorConditionSerializerError(
                str(e),
                Configuration.MODELS_ERROR,
                f"VendorConditionSerializerError.{__class__.__name__}"
            )

    def get_menu_items_data(self, menu_id: int) -> MenuItem:
        return MenuItem.objects.get(id=menu_id)

    def get_menu_items_status_data(self, menu_id: int, vendor_id: int) -> MenuStatus:
        if self.test:
            return MenuStatus.generate_faker_status(menu_id=menu_id, vendor_id=vendor_id)
        menu_item = MenuItem.objects.get(id=menu_id)
        return MenuStatus.get_today_status(menu_item=menu_item)

    def get_vendor_data(self, vendor_id: int) -> Vendor:
        self.vednor = Vendor.get_vendor(vendor_id)
        return self.vednor

    def get_customer_data(self, uid: str) -> Customer:
        self.customer = Customer.objects.get(uid=uid)
        return self.customer

    @staticmethod
    def get_model_data(model: models.Model, id: int) -> models.Model:
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            raise Vendor.DoesNotExist(
                f"{model.__class__.__name__} with id {id} does not exist")

    def get_printer_request_data(self):
        """只能在 test case 使用！"""
        o = Order.objects.get(id=1)

        serializer = OrderRequestBodySerializer(
            data=self.get_json_order_data())
        serializer.is_valid(raise_exception=True)

        o.confirmation_hash = Tool.hash_data(o)

        o.save()

        order_items = self.create_order_items(
            serializer.validated_data.get("order_items"), o)

        return o, order_items
