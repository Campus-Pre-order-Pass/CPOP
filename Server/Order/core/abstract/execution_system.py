from abc import ABC, abstractmethod


class ExecutionSystem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute_order(self, order):
        pass
