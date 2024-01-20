from Order.core.module.configuration import Configuration
from Order.core.module.error.error import BaseError


class ConditionsError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class OrderCreationError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class StrategyModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class RiskManagementModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class DataCheckModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None):
        super().__init__(message, error_code, error_source)


class ExecutionModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class DataModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class BacktestModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class AccountModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class LogAndMonitorModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class EventManagementModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)


class PrintDocumentModuleError(BaseError):
    def __init__(self, message, error_code, error_source=None, *args, **kwargs):
        super().__init__(message, error_code, error_source)
