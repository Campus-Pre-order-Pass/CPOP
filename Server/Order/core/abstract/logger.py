
from abc import ABC, abstractmethod


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
