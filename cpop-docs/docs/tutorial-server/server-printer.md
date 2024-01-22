---
id: server-printer
title: 印單機
sidebar_label: 印單機
sidebar_position: 2
---

## 規格

# input

```json
{
  "vendor_id": 1,
  "customer_id": 1,
  "order_items": [
    {
      "menu_item_id": 36,
      "required_option_ids": [1, 2],
      "extra_option_ids": [1, 2],
      "quantity": 4
    },
    {
      "menu_item_id": 2,
      "required_option_ids": [3, 4],
      "extra_option_ids": [3, 4],
      "quantity": 3
    }
  ]
}
```

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