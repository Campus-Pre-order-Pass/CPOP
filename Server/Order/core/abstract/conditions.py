from abc import ABC, abstractmethod


class ConditionsModule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def check_data_from_condition(self):
        pass

    @abstractmethod
    def check_vendor_condition(self):
        pass

    @abstractmethod
    def handle_error_conditions(self, error):
        pass
