# mdoels
from Order.models import OrderItem
from MenuItem.models import ExtraOption, MenuItem, RequiredOption

# SettingsManager
from Order.OrderLogic.setting import SettingsManager

# tool
from Order.OrderLogic.helper.tool import Tool


from decimal import Decimal

from Order.OrderLogic.error.error import OrderCreationError


class Helper:
    @staticmethod
    def get_total_amount(order_items: any) -> float:
        try:
            total = Decimal('0.0')

            for order_item in order_items:
                required_option_total = Decimal('0.0')
                extra_option_total = Decimal('0.0')

                quantity = order_item.get('quantity')
                menuItem = MenuItem.objects.get(
                    id=order_item.get('menu_item_id'))
                required_option_ids = order_item.get('required_option_ids', [])
                extra_option_ids = order_item.get('extra_option_ids', [])

                if not Tool.is_positive_integer(quantity):
                    raise OrderCreationError("Invalid quantity for order item")

                if not Tool.is_positive_float(menuItem.price):
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
            raise OrderCreationError(str(e), SettingsManager.ERROR_CODE)
