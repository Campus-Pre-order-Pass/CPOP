
from datetime import datetime
import pytz
import inspect


class Tool():
    @staticmethod
    def get_now_time_taipei(timezone: str = "Asia/Taipei"):
        return datetime.now(pytz.timezone(timezone)).time()


tool = Tool()
