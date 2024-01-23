import json
from django.test import Client
from django.urls import reverse
from faker import Faker
from datetime import date
from django.utils import timezone

# models
from Shop.models import *

# tasks
from Shop.tasks import creat_shop_daily_instance

# TestAPIBaseCase
from helper.base.base_test_case import TestAPIBaseCaseV2
# Create your tests here.

fake = Faker('zh_TW')


class TestAPIView(TestAPIBaseCaseV2):
    VEDNOR_ID = 1
    BASE_URL = "/v0/api/shop/"

    def test_ShopAPIView(self):
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL
        url = reverse("Shop:shop_list")

        # 发起 GET 请求
        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    def test_CurrentStateAPIView(self):
        # creat_shop_daily_instance()
        tomorrow = timezone.now().date() + timezone.timedelta(days=1)

        CurrentState.objects.create(
            id=1000,
            vendor=Vendor.objects.get(id=1),
            shopping_type="online",
            date=tomorrow,
            current_number=fake.random_int(min=1, max=100),
            wait_number=fake.random_int(min=0, max=50),
            is_start=fake.boolean(),
            is_delivery_available=fake.boolean()
        )
        # 创建一个 Django Client 实例
        client = Client()

        # 使用 reverse 获取 URL，并传递参数
        url = self.reverse("Shop:current", vendor_id=1)

        # 发起 GET 请求
        response = client.get(url, content_type="application/json")

        if response.status_code != 200:
            print("Unexpected response status code:", response.status_code)
            print("Response content:", response.content.decode(
                'utf-8'))  # 解码响应内容并打印

        # 检查响应状态码是否是 200 OK
        self.assertEqual(response.status_code, 200)

    # def test_update_current_state(self):
    #     # 创建一个 CurrentState 对象
    #     tomorrow = timezone.now().date() + timezone.timedelta(days=1)

    #     current_state = CurrentState.objects.create(
    #         id=1000,
    #         vendor=Vendor.objects.get(id=1),
    #         shopping_type="online",
    #         date=tomorrow,
    #         current_number=fake.random_int(min=1, max=100),
    #         wait_number=fake.random_int(min=0, max=50),
    #         is_start=fake.boolean(),
    #         is_delivery_available=fake.boolean()
    #     )

    #     # 构建更新数据
    #     update_data = {
    #         "shopping_type": "physical",
    #         "current_number": "100",
    #     }

    #     url = self.reverse("Shop:current", vendor_id=1)

    #     # 发起 PATCH 请求，并提供更新数据
    #     response = self.client.patch(
    #         path=url, data=update_data,  format="json")

    #     # 验证响应
    #     TestAPIBaseCaseV2.is_available(response)
    #     # self.printer.print_green(response.content)
    #     self.assertEqual(response.status_code, 200)

    #     # 验证数据库中的对象是否被成功更新
    #     updated_current_state = CurrentState.objects.get(id=current_state.id)
    #     self.assertEqual(updated_current_state.shopping_type, "physical")
    #     self.assertEqual(updated_current_state.current_number, 100)

    #     # 验证其他更新后的字段


class TaskTestCase(TestAPIBaseCaseV2):
    def test_tasks(self):
        CurrentState.objects.all().delete()
        VendorDailyMetrics.objects.all().delete()

        creat_shop_daily_instance()
