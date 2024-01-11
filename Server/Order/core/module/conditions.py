from Order.core.abstract.conditions import ConditionsModule as abc
# base
from Order.core.module.base import BaseClass

# error


class Conditions(abc, BaseClass):
    def __init__(self, *args, **kwargs):
        pass

    def check_data_from_condition(self, data):
        pass

    def check_vendor_condition(self):
        pass

    def handle_error_conditions(self, error):
        pass

    def __str__(self) -> str:
        # to string
        return str(self.Version)
