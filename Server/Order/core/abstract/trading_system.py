from abc import ABC, abstractmethod


class TradingSystem(ABC):
    @abstractmethod
    def __init__(self):
        """
        抽象方法 - 初始化方法，負責建立交易系統的基本結構。
        """
        pass

    @abstractmethod
    def subscribe_events(self):
        """
        抽象方法 - 設定事件訂閱，建立模塊之間的通信機制。
        """
        pass

    @abstractmethod
    def load_configuration(self, config_file_path):
        """
        抽象方法 - 載入配置文件，確保交易系統參數和設定的正確性。

        :param config_file_path: 配置文件的路徑。
        """
        pass

    @abstractmethod
    def run_backtest(self, start_date, end_date):
        """
        抽象方法 - 運行回測，模擬交易策略在歷史數據上的表現。

        :param start_date: 回測起始日期。
        :param end_date: 回測結束日期。
        """
        pass


class EventManagement(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass


class ConfigurationModule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_configuration(self, file_path):
        pass
