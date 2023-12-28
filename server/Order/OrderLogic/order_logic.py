import hashlib
import secrets


# models
from ..models import Order, OrderItem

# hash
from Order.OrderLogic.hash.hash import HashTool

# mark
from Order.OrderLogic.test.mark import MarkData


class OrderLogic:
    """交易系統的邏輯"""

    V = "0"

    # _instance = None  # 類變量，用於保存實例

    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         # 如果實例還不存在，則創建一個新的實例
    #         cls._instance = super().__new__(cls)
    #         # 在這裡進行初始化/配置
    #         cls._instance.config = cls._load_config()
    #     return cls._instance

    @staticmethod
    def create_order(data):
        # 处理创建订单的逻辑，例如从传入的数据中获取订单信息并保存到数据库
        # 这里只是一个示例，你需要根据实际情况来编写具体的逻辑

        # 在这里添加哈希加密逻辑
        hashed_customer_name = HashTool.hash_data(
            data.get('customer_name', ''))
        data['customer_name'] = hashed_customer_name
        # 其他逻辑...

        # 在订单确认后生成随机哈希值
        confirmation_hash = HashTool.generate_confirmation_hash()
        data['confirmation_hash'] = confirmation_hash

        # 保存订单到数据库
        Order.objects.create(**data)

    @staticmethod
    def cancel_order(order: Order):
        pass

    @staticmethod
    def get_order_list():
        # 处理获取订单列表的逻辑，例如从数据库中获取订单数据
        # 这里只是一个示例，你需要根据实际情况来编写具体的逻辑
        pass

    def save_order_log(slef):
        pass

    @staticmethod
    def test_order():
        MarkData.get_data()
        pass
