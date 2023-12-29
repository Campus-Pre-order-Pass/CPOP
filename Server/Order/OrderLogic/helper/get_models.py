

from Order.OrderLogic.setting import SettingsManager

# models
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model, QuerySet

from MenuItem.models import ExtraOption, MenuItem, RequiredOption
from Order.models import OrderItem, Order

from Order.OrderLogic.error.error import OrderCreationError


class ModelManager:
    """管理mdoels與"""
    @staticmethod
    def creat_model_instance(model_class: Model, id: int) -> QuerySet:
        try:
            # 使用 objects.get() 获取模型实例
            return model_class.objects.get(id=id)
        except ObjectDoesNotExist:
            raise OrderCreationError(
                f"{model_class.__name__} not found for the given id.", code=SettingsManager.MODELS_NOT_FOUND)
        except Exception as e:
            # 捕捉其他可能的异常
            raise OrderCreationError(
                f"An error occurred while retrieving {model_class.__name__}: {str(e)}", code=SettingsManager.MODELS_ERROR)

    @staticmethod
    def create_order_items(order_items: any, order: Order) -> any:
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
                menuItem=ModelManager.creat_model_instance(
                    model_class=MenuItem, id=menu_item_id),
                quantity=quantity
            )

            # Add ExtraOption and RequiredOption instances to OrderItem
            order_item_instance.extra_option.set(extra_options)
            order_item_instance.required_option.set(required_options)

            # Append the created OrderItem instance to the list
            created_order_items.append(order_item_instance)

        return created_order_items
