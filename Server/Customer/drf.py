# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# rest_framework
from rest_framework import status
from rest_framework.views import APIView

# MarkData
from Order.OrderLogic.test.mark import MarkData
from MenuItem.serializers import MenuItemExtraOptionSerializer, MenuItemRequiredOptionSerializer, MenuItemSerializer

# BaseAPIViewDRFConfig
from helper.base.drf_yasg_base import BaseAPIViewDRFConfig

# serializers
from Order.serializers import OrderItemSerializer, OrderRequestBodySerializer, OrderSerializer
from Customer.serializers import CustomerSerializerSerializer

uid_param = openapi.Parameter(
    name="uid",
    in_=openapi.IN_PATH,
    type=openapi.TYPE_STRING,
    description="顧客 `UID`",
    required=True,
    example="test",
)


class DRF(APIView):
    """drf_yasg app configuration"""
    CustomerAPIView = {
        "GET": {
            "operation_summary": "獲取顧客",
            "operation_description": "獲取顧客",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                uid_param
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="獲取回傳使用者資料",
                    schema=CustomerSerializerSerializer()
                ),
            }
        },
        "POST": {
            "operation_summary": "新增顧客",
            "operation_description": "新增顧客`",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                BaseAPIViewDRFConfig.X_CSRF_TOKEN_BASE_HEADER,
                uid_param
            ],
            "request_body": CustomerSerializerSerializer(),
            "responses": {
                status.HTTP_201_CREATED: openapi.Response(
                    description="獲取回傳使用者資料",
                    schema=CustomerSerializerSerializer()
                    # examples=
                ),
                status.HTTP_400_BAD_REQUEST: openapi.Response(
                    description="serializers error")
            }
        },
        "PATCH": {
            "operation_summary": "修改顧客",
            "operation_description": (
                "使用 PATCH 方法修改顧客名稱。請使用 JSON 格式提供要修改的數據。\n\n"
                "示例 JSON 數據:\n"
                "```json\n"
                "{\n"
                '  "name": "newname"\n'
                "}\n"
                "```\n"
                "不需要給完整資料即可!\n"

            ),            'manual_parameters': [BaseAPIViewDRFConfig.FIRE_BASE_HEADER, uid_param],
            "request_body": CustomerSerializerSerializer(),
            "responses": {
                status.HTTP_201_CREATED: openapi.Response(
                    description="獲取回傳使用者資料",
                    schema=CustomerSerializerSerializer()
                    # examples=
                ),
                status.HTTP_400_BAD_REQUEST: openapi.Response(
                    description="serializers error")
            }
        },
        "DELETE": {
            "operation_summary": "刪除顧客除",
            "operation_description": "刪除顧客`",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                uid_param
            ],
            "responses": {
                status.HTTP_204_NO_CONTENT: openapi.Response(
                    description="刪除成功",
                )
            }
        }
    }
