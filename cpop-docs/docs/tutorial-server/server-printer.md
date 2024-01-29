---
id: server-printer
title: 印單機
sidebar_label: 印單機
sidebar_position: 2
---

## 規格

# is_connected Method

# 位置:`server/order/core/modue/printer.py`

### Parameters

- **self**: The instance of the class containing this method.
- **order (Order)**: An instance of the `Order` class used for checking the connection.
- **order_items (OrderItem)**: An instance of the `OrderItem` class used for checking the connection.

### Returns

- **bool**: 回傳是否可以連線 如果不行就用 raise

### Raises

需要繼承`BaseError`來做 raise，在`server/order/core/modue/error/error.py`裡面

- **CustomException**: 需要寫 conf and erro code 定義，在`cpop-docs/docs/tutorial-server/server-printer.md`裡面

### abstractmethod

````python

from abc import ABC, abstractmethod


class Printer(ABC):
    """抽象類別，繼承此類別

    ```python
        p = Printer(order)
        if p.is_valid() & p.is_connected():
            p.print()
    ```
    """
    OK_CODE = 200
    ERROR_CODE = 500

    def __init__(self, order, *args, **kwargs):
        self.test = kwargs.pop('test', False)
        self.order = order

    @abstractmethod
    def is_valid(self) -> bool:
        """先判斷是否資料格式正確，需要做`raise報錯`

        Returns:
            bool: _description_
        """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """先判斷是否印單機有連線,需要做`raise報錯`

        Returns:
            bool: _description_
        """
        pass

    @abstractmethod
    def print(self):
        """_summary_
        """
        # Your print logic here
        pass


````

# 測試環節

位置: `server/order/tests.py`

**注意:** 必須先使用虛擬環境！

執行測試指令：

```bash
python manage.py test Order.tests.OrderPrinter.test_printer
```
