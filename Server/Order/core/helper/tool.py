
from datetime import datetime
import pytz
import inspect
import hashlib
import secrets
from django.core.serializers import serialize

from Order.OrderLogic.setting import SettingsManager
from Order.OrderLogic.error.error import OrderCreationError

# error handling
from Order.core.module.error.error import BaseError


class Tool():
    @staticmethod
    def get_now_time_taipei(timezone: str = "Asia/Taipei"):
        return datetime.now(pytz.timezone(timezone)).time()

    @staticmethod
    def is_positive_integer(value: int) -> int:
        try:
            # Try to convert the value to an integer
            integer_value = int(value)

            # Check if the integer is positive
            if integer_value > 0:
                return True
            else:
                return False

        except ValueError:
            raise ValueError("It's not a positive integer",
                             SettingsManager.ERROR_CODE)

    @staticmethod
    def is_positive_float(value: float) -> bool:
        try:
            # Try to convert the value to a float
            float_value = float(value)

            # Check if the float is positive
            if float_value > 0:
                return True
            else:
                return False

        except ValueError:
            # If the conversion to float fails, raise a ValueError
            raise OrderCreationError("It's not a positive float",
                                     SettingsManager.ERROR_CODE,
                                     f"{Tool.__class__.__name__}.is_positive_float")

    @staticmethod
    def hash_data(data: any):
        """
        使用 SHA-256 对数据进行哈希加密
        """
        serialized_data = serialize('json', [data])

        sha256 = hashlib.sha256()
        sha256.update(serialized_data.encode('utf-8'))
        return sha256.hexdigest()

    @staticmethod
    def generate_confirmation_hash():
        """
        生成随机哈希值
        """
        random_string = secrets.token_urlsafe(16)  # 生成一个16字节的随机字符串
        return Tool.hash_data(random_string)


def check_test_decorator(func):
    def wrapper(self, *args, **kwargs):
        if self.test:
            return True
        else:
            return func(self, *args, **kwargs)

    return wrapper


def handle_order_creation_error_v0(error_code: int = 999, error_class: BaseError = BaseError):
    """_summary_

    Args:
        error_code (int): _description_
        error_class (BaseError, optional): _description_. Defaults to BaseError.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BaseError as e:
                calling_function = inspect.currentframe().f_back.f_code.co_name
                raise error_class(
                    str(e),
                    error_code,
                    calling_function
                ) from e

        return wrapper

    return decorator
