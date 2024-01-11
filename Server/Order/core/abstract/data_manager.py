from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def __init__(self, mock_path: str):
        pass

    @abstractmethod
    def fetch_market_data(self):
        pass

    @abstractmethod
    def fetch_test_send_data(self):
        pass

    @abstractmethod
    def fetch_test_result_data(self):
        pass
