import hashlib
import secrets
from django.core.serializers import serialize


class HashTool():
    @staticmethod
    def hash_data(data):
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
        return HashTool.hash_data(random_string)
