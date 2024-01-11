import datetime


class Valid():
    """_Valid_

    ```python

    try:
        assert Valid.is_integer(10)
        print("10 是整數")
    except ValueError as e:
        print(e)

    try:
        assert Valid.is_integer(10.5)
        print("10.5 是整數")
    except ValueError as e:
        print(e)    
    ```
    """
    @staticmethod
    def is_integer(n):
        """_summary_

        Args:
            n (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if not isinstance(n, int):
            raise ValueError(f"{n} 不是整數")
        return True

    @staticmethod
    def is_positive(n):
        """_summary_

        Args:
            n (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if n <= 0:
            raise ValueError(f"{n} 不是正數")
        return True

    @staticmethod
    def is_today(date: datetime.date, tz):
        """_summary_

        Args:
            date (datetime.date): _description_
            timezone (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        today = datetime.now(tz).date()
        if date != today:
            raise ValueError(f"{date} 不是今天")
        return True
