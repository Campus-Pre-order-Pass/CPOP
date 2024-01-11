# django
import django

from typing import Self
from Order.core.module.base import BaseClass


class BaseTradingSystem(BaseClass):
    Version = "1.0"

    def __init__(self, *args, **kwargs):
        super(BaseTradingSystem, self).__init__(*args, **kwargs)
        django.setup()

        self.order = None

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return super().__str__()

    def __getitem__(self, key: str) -> str:
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
