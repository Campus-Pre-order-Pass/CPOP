from abc import ABC, abstractmethod


class AbstractOrderLogic(ABC):
    @abstractmethod
    def setTest(self, value) -> bool:
        """
        Set the test mode for the order logic.

        Parameters:
        - value (bool): True to enable test mode, False otherwise.
        """
        pass

    @abstractmethod
    def test_order(self) -> any:
        """
        Generate test order data.

        Returns:
        dict: Test order data.
        """
        pass

    @abstractmethod
    def check_order(self) -> bool:
        """
        Check the validity of the order.

        Returns:
        dict: Validated order data.
        """
        pass

    @abstractmethod
    def create_order(self) -> str:
        """
        Create an order.

        Returns:
        Order: Created order instance.
        """
        pass


class OrderVaild(ABC):
    pass
