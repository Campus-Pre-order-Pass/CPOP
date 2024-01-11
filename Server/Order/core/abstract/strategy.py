
from abc import ABC, abstractmethod


class RiskManager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def manage_risk(self, trade):
        pass
