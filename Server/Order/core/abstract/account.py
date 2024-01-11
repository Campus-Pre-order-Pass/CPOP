from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update_account_status(self, trade):
        pass
