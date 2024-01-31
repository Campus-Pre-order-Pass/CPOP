# django
import django

from Order.core.module.base import BaseClass
from Order.core.module.conditions import Conditions
from Order.core.module.logger import Logger
from Order.core.module.execution_system import ExecutionSystem
from Order.core.module.printer import Printer


class BaseTradingSystem(BaseClass):

    def __init__(self, *args, **kwargs):
        super(BaseTradingSystem, self).__init__(*args, **kwargs)

        django.setup()

        self.order = None

        # module
        self.conditions = Conditions(*args, **kwargs)

        self.logger = Logger(*args, **kwargs)

        self.execution_system = ExecutionSystem(*args, **kwargs)

        self.printer = Printer(*args, **kwargs)

    def __repr__(self) -> str:
        pass

    def __getitem__(self, key: str) -> str:
        """_summary_

        Args:
            key (str): _description_

        Raises:
            KeyError: _description_

        Returns:
            str: _description_
        """
        if key in self.order:
            return self.order[key]
        else:
            raise KeyError(f"Key '{key}' not found in the order")

    def __format__(self, format_spec: str) -> str:
        # 計算 self.order 的 hash 值
        hash_value = hash(self.order) if self.order is not None else 0

        # 根據 format_spec 返回格式化後的結果
        formatted_result = f"Formatted Result: {hash_value} ({format_spec})"
        return formatted_result
