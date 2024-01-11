from abc import ABC, abstractmethod


class TradingSystem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def subscribe_events(self):
        pass

    @abstractmethod
    def load_configuration(self):
        pass

    @abstractmethod
    def run_backtest(self):
        pass


class Strategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def generate_signals(self, market_data):
        pass

    @abstractmethod
    def execute_trades(self, signals):
        pass


class ExecutionSystem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute_order(self, order):
        pass


class DataManager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fetch_market_data(self, symbol, start_date, end_date):
        pass


class Backtester(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def simulate_trading(self, strategy, market_data):
        pass


class EventManagement(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass


class Account(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update_account_status(self, trade):
        pass


class LoggingAndMonitoring(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def log_system_event(self, event):
        pass

    @abstractmethod
    def monitor_system_status(self):
        pass


class ConfigurationModule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_configuration(self, file_path):
        pass


class ConditionsModule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle_error_conditions(self, error):
        pass


class ConfigurationError(Exception):
    pass
