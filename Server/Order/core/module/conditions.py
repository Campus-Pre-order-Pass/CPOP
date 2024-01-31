# base
from Order.core.module.base import BaseClass
from Order.core.module.configuration import C
from Shop.models import *

# serializers
from Order.core.module.serializers import OrderRequestBodySerializer

from .error.configuration_error import OrderCreationError
from Order.core.helper.tool import check_test_decorator, handle_order_creation_error_v0
from Order.core.module.order_vaild import OrderVaild


class Conditions(BaseClass):
    def __init__(self, *args, **kwargs):
        super(Conditions, self).__init__(*args, **kwargs)
        self.order_valid = OrderVaild(*args, **kwargs)

    @handle_order_creation_error_v0(
        error_code=C.VAILD_ERROR,
        error_class=OrderCreationError,
    )
    def check_data_format_condition(self, data: dict) -> OrderRequestBodySerializer:
        self.order = OrderRequestBodySerializer(data=data)
        if self.order.is_valid():
            pass
        else:
            raise Exception(self.order.errors)

        return self.order

    @check_test_decorator
    @handle_order_creation_error_v0(
        error_code=C.VAILD_ERROR,
        error_class=OrderCreationError,
    )
    def check_system_condition(self) -> bool:
        """檢查系統預設條件"""

        return True

    @check_test_decorator
    @handle_order_creation_error_v0(
        error_code=C.VAILD_ERROR,
        error_class=OrderCreationError,
    )
    def check_vendor_condition(self) -> bool:
        """檢查店家條件
        """

        validations = [
            lambda: self.order_valid.check_daily_purchase_limit(self.order),
            lambda: self.order_valid.check_business_hours(
                vendor_id=self.order.validated_data.get('vendor_id')
            ),
            lambda: self.order_valid.check_user_purchase_limit(
                self.order.validated_data.get("uid")),
            lambda: self.order_valid.check_customer_take_time(
                self.order.validated_data.get("take_time"))

        ]

        [validation() for validation in validations]

        return True

    # @check_test_decorator
    @handle_order_creation_error_v0(
        error_code=C.VAILD_ERROR,
        error_class=OrderCreationError,
    )
    def check_menu_items_condition(self) -> bool:
        """檢查菜單條件"""

        order_items = self.order.validated_data.get("order_items")

        validations = [
            lambda item, vendor_id: self.order_valid.check_menu_items_inventory(
                item, vendor_id)
        ]

        for item in order_items:
            [validation(item, self.order.validated_data.get("vendor_id"))
             for validation in validations]

        return True

    def __str__(self) -> str:
        # to string
        return str(self.Version)
