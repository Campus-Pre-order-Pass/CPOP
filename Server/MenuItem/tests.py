from django.test import TestCase
from django.test import Client
from django.urls import reverse

# TestAPIBaseCase
from helper.base.base_test_case import TestAPIBaseCase

# Create your tests here.


vendor_id = 1
uid = "1"

menu_id = "1"


class TestAPIView(TestAPIBaseCase):
    def test_CurrentStateAPIView(self):
        client = Client()

        # 使用 reverse 获取 URL
        url = reverse("MenuItem:VendorAPIView", args=[uid])

        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    def test_OptionPIView(self):
        client = Client()

        # 使用 reverse 获取 URL
        url = reverse("MenuItem:ExtraOptionPIView", args=[menu_id])

        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)
