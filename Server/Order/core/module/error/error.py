from Order.core.module.configuration import Configuration


class BaseError(Exception):
    def __init__(self, message: str, error_code: int | None, error_source=str | None, *args, **kwargs):
        super().__init__(message)
        self.code = error_code
        self.error_source = ""

        if kwargs.pop('test', False):
            self.error_source = error_code


# tools

class NotFoundModuleError(BaseError):
    def __init__(self, message: str,  error_source=None,  *args, **kwargs):
        super().__init__(f"{message} not found",
                         Configuration.MODELS_NOT_FOUND, error_source, args, kwargs)
