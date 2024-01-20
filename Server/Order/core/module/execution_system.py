from decimal import Decimal

# base
from Order.core.module.base import BaseClass

# serializers
from Order.core.module.serializers import OrderRequestBodySerializer

from MenuItem.models import ExtraOption, MenuItem, RequiredOption
from Order.core.module.error.configuration_error import OrderCreationError


class ExecutionSystem(BaseClass):
    def __init__(self, *args, **kwargs):
        super(ExecutionSystem, self).__init__(*args, **kwargs)

    def change_menu_state(self, data: OrderRequestBodySerializer):
        order_items = data.validated_data["order_items"]
        vendor_id = data.validated_data["vendor_id"]

        for order_item_data in order_items:
            menu_item_id = order_item_data.get("menu_item_id")
            menu_item = self.data_manager.get_menu_items_status_data(
                menu_item_id, vendor_id)

            menu_item.remaining_quantity -= 1
            menu_item.save()

    def calculate(self, data: OrderRequestBodySerializer) -> float:
        try:
            total = Decimal('0.0')
            order_items = data.validated_data["order_items"]

            for order_item in order_items:
                required_option_total = Decimal('0.0')
                extra_option_total = Decimal('0.0')

                quantity = order_item.get('quantity')
                menuItem = MenuItem.objects.get(
                    id=order_item.get('menu_item_id'))
                required_option_ids = order_item.get('required_option_ids', [])
                extra_option_ids = order_item.get('extra_option_ids', [])

                if not self.tool.is_positive_integer(quantity):
                    raise OrderCreationError("Invalid quantity for order item")

                if not self.tool.is_positive_float(menuItem.price):
                    raise OrderCreationError("Invalid price for menu item")

                # 計算必選選項總價格
                for required_option_id in required_option_ids:
                    extraOption = ExtraOption.objects.get(
                        id=required_option_id)
                    extra_option_total += extraOption.price * quantity

                # 計算額外選項總價格
                for extra_option_id in extra_option_ids:
                    requiredOption = RequiredOption.objects.get(
                        id=extra_option_id)
                    required_option_total += requiredOption.price * quantity

                total += quantity * menuItem.price + extra_option_total + required_option_total

            return total
        except Exception as e:
            raise OrderCreationError(str(e), self.configuration.ERROR_CODE)
