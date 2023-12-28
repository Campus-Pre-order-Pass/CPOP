from Order.OrderLogic.setting import SettingsManager


class Tool():
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
            raise ValueError("It's not a positive float",
                             SettingsManager.ERROR_CODE)
