from faker import Faker
from rest_framework.test import APITestCase
from rest_framework import status

from helper.base.base_test_case import TestAPIBaseCaseV2

base_url = '/v0/api/c/'

fake = Faker('zh_TW')


class TestAPIView(TestAPIBaseCaseV2):
    def test_get_customer(self):
        # 模拟 GET 请求
        response = self.client.get(path=f"{base_url}test")  # 请替换为实际的 API URL
        TestAPIView.is_available(response=response)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 验证其他期望的 GET 行为

    def test_create_customer(self):
        # 模拟 POST 请求
        # 请替换为实际的 POST 数据
        data = {
            "uid": fake.uuid4(),
            "name":  fake.name(),
            "contact": fake.phone_number(),
            "email": fake.email(),
        }

        response = self.client.post(
            f"{base_url}", data, format='json')  # 请替换为实际的 API URL

        TestAPIView.is_available(response, status.HTTP_201_CREATED)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_customer(self):
        self.test_create_customer()

        id = "test"

        # 模拟 PATCH 请求（部分更新）
        update_data = {'name': 'Updated Name', 'email': 'updated@example.com'}
        update_response = self.client.patch(
            f'{base_url}{id}', update_data, format='json')

        TestAPIView.is_available(update_response)

        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        # 验证其他期望的 PATCH 行为

    def test_delete_customer(self):
        self.test_create_customer()

        id = "test"

        update_response = self.client.delete(
            f'{base_url}{id}', format='json')

        TestAPIView.is_available(update_response, 204)

        self.assertEqual(update_response.status_code,
                         status.HTTP_204_NO_CONTENT)
