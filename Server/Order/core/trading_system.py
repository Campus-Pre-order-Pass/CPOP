from Order.core.base.base_trading_system import BaseTradingSystem


class TradingSystem(BaseTradingSystem):
    def __init__(self, *args, **kwargs):
        super(TradingSystem, self).__init__(*args, **kwargs)
