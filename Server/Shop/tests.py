from django.test import TestCase
from django.test import Client
from django.urls import reverse

# TestAPIBaseCase
from helper.base.base_test_case import TestAPIBaseCase
# Create your tests here.


class TestAPIView(TestAPIBaseCase):
    def test_ShopAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL
        url = reverse("Shop:shop")

        # 发起 GET 请求
        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    def test_CurrentStateAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL，并传递参数
        vendor_id = "1"
        url = reverse("Shop:current", args=[vendor_id])

        # 发起 GET 请求
        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)
