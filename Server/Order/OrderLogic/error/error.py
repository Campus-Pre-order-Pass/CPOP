class CustomError(Exception):
    """Custom exception class for your specific errors."""
    pass


class ErrorHandler:
    @staticmethod
    def raise_custom_error(message):
        """Raise a custom error with the provided message."""
        raise CustomError(message)


# # Example of using the custom error handler
# try:
#     ErrorHandler.raise_custom_error("This is a custom error message.")
# except CustomError as e:
#     print(f"Caught an error: {e}")
