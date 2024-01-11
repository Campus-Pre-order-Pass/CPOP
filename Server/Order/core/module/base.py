class BaseClass(object):
    """base class and tools

    Args:
        object (_type_): _description_
    """

    Version = "0.0"

    def __init__(self, *args, **kwargs):

        self.test = kwargs.pop('test', False)

    def __call__(self, *args, **kwargs):
        """_call method_
        """
        print(f"參數：{args}, 關鍵字參數：{kwargs}")
