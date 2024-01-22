from Order.core.base.base_trading_system import BaseTradingSystem

# mdoels
from Order.models import Order


class TradingSystem(BaseTradingSystem):
    def __init__(self,  *args, **kwargs):
        super(TradingSystem, self).__init__(*args, **kwargs)

    def setData(self, data: dict):
        # check conditions
        self.conditions.check_system_condition()

        self.order = self.conditions.check_data_format_condition(data=data)

        self.conditions.check_vendor_condition()

        self.conditions.check_menu_items_condition()

    def execute(self) -> str:
        if self.order == None:
            raise ValueError("setData must be called before executing.")

        o = Order(
            vendor=self.data_manager.get_vendor_data(
                self.order.validated_data.get('vendor_id')),
            customer=self.data_manager.get_customer_data(
                self.order.validated_data.get("customer_id")),
            # order_time=self.tool.get_now_time_taipei(),
            take_time=self.order.validated_data.get("take_time"),
            total_amount=self.execution_system.calculate(data=self.order),
            order_status="created",
        )

        o.confirmation_hash = self.tool.hash_data(o)

        # printer

        if self.printer.is_connected(self.order):
            self.printer.print()

        # TODO: 要改
        o.order_status = "processing"
        o.save()
        # if self.test:
        #     order.show()

        self.data_manager.create_order_items(
            self.order.validated_data.get("order_items"), o)

        # 減少庫存
        self.execution_system.change_menu_state(data=self.order)

        return o.confirmation_hash
