class BaseError(Exception):
    def __init__(self, message, error_code, error_source=None):
        super().__init__(message)
        self.code = error_code
        self.error_source = error_source


class OrderCreationError(BaseError):
    def __init__(self, message, error_code, error_source=None):
        super().__init__(message, error_code, error_source)


class VendorConditionSerializerError(BaseError):
    def __init__(self, message, error_code, error_source=None):
        super().__init__(message, error_code, error_source)
