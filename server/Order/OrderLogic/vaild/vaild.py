from ...models import Order, FoodItem


class OrderVaild():
    @staticmethod
    def validate_order_models(self, order: Order):
        "檢查 order 格式是否正確"
        pass

    @staticmethod
    def is_order_valid(order):
        """
        检查订单对象是否有效
        """
        if not isinstance(order, Order):
            return False

        # 在这里添加其他验证逻辑，例如检查必填字段是否存在、关联关系等
        # 以下是一个示例，你需要根据实际情况来编写具体的验证逻辑

        if not order.customer_name or not order.total_amount or not order.confirmation_hash:
            return False

        # 添加其他验证逻辑...

        return True

    @staticmethod
    def check_food_quantity(food_item_id, quantity):
        """
        检查剩余食物数量是否足够
        """
        try:
            food_item = FoodItem.objects.get(pk=food_item_id)
        except FoodItem.DoesNotExist:
            return False  # 食物项不存在

        # 在这里添加检查剩余食物数量的逻辑
        # 以下是一个示例，你需要根据实际情况来编写具体的逻辑

        return food_item.remaining_quantity >= quantity
