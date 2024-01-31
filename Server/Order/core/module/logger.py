from Order.core.module.base import BaseClass

# models
from Order.models import TransactionLog
from Customer.models import Customer


class Logger(BaseClass):
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)

    def make_logger(self, uid: str, action: str, details: str = None, *args, **kwargs):
        c = Customer.objects.get(uid=uid)
        TransactionLog.objects.create(
            customer=c,
            action=action,
            details=details,
        )
