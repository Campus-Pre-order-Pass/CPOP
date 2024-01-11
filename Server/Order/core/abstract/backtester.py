from abc import ABC, abstractmethod


class Backtester(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def simulate_trading(self, strategy, market_data):
        pass
