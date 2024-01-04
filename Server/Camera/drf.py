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

    upload_image = {
        "PATCH": {
            "operation_summary": "上傳圖片",
            "operation_description": ("上傳圖片並用`opencv`分析，更改現在餐廳號碼 \n" "**需要把把照片轉二進制**"),
            "request_body": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                required=['image', 'storeID'],
                properties={
                    'image': openapi.Schema(type=openapi.TYPE_STRING, format='binary', description="要上傳的圖片文件"),
                    'storeID': openapi.Schema(type=openapi.TYPE_STRING, description="商店 `ID`"),
                },
            ),
            "consumes": ['multipart/form-data'],
            "responses": {
                status.HTTP_200_OK: openapi.Response(description="成功上傳圖片"),
                status.HTTP_400_BAD_REQUEST: openapi.Response(description="請求無效"),
            },
        },
    }
