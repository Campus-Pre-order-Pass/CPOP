# mdoels
from Order.models import OrderItem
from MenuItem.models import MenuItem

# SettingsManager
from Order.OrderLogic.setting import SettingsManager

# tool
from Order.OrderLogic.helper.tool import Tool


class Helper:
    @staticmethod
    def get_total_amount(order_items: [OrderItem]) -> float:
        total = 0.0

        for order_item in order_items:
            if not Tool.is_positive_integer(order_item.quantity):
                raise ValueError("Invalid quantity for order item")

            if not Tool.is_positive_float(order_item.menuItem.price):
                raise ValueError("Invalid price for menu item")

            total += float(order_item.quantity) * \
                float(order_item.menuItem.price)

        return total
