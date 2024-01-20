from abc import ABC, abstractmethod


class PrinterABC(ABC):
    """抽象類別，繼承此類別

    ```python
        p = Printer(order)
        if p.is_valid() & p.is_connected():
            p.print()
    ```
    """
    OK_CODE = 200
    ERROR_CODE = 500

    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', False)

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
