
from datetime import datetime
import pytz


def check_condition_decorator(func):
    def wrapper(*args, **kwargs):
        # 在这里添加你的条件检查逻辑
        if condition_not_met:
            print("Condition not met. Function will not be executed.")
            return None  # 或者抛出异常，或者进行其他适当的处理
        else:
            # 条件满足，执行原始函数
            return func(*args, **kwargs)

    return wrapper


def check_taiwan_weekend_decorator(func):
    def wrapper(*args, **kwargs):
        # 获取当前时间
        current_time_utc = datetime.utcnow()

        # 设置台湾时区
        taipei_timezone = pytz.timezone('Asia/Taipei')
        current_time_taipei = current_time_utc.replace(
            tzinfo=pytz.utc).astimezone(taipei_timezone)

        # 获取今天是星期几，0表示星期一，6表示星期日
        today = current_time_taipei.weekday()

        if today in [5, 6]:  # 如果是星期五或星期六，不执行函数
            print("It's the weekend in Taiwan. Function will not be executed.")
            return None  # 或者抛出异常，或者进行其他适当的处理
        else:
            # 条件不满足，执行原始函数
            return func(*args, **kwargs)

    return wrapper
