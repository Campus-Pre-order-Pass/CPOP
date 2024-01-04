# swagger
from datetime import date
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# rest_framework
from rest_framework import status

# BaseAPIViewDRFConfig
from helper.base.drf_yasg_base import BaseAPIViewDRFConfig

# serializers
from Shop.serializers import VendorSerializer, CurrentStateSerializer


class DRF:
    """drf_yasg app configuration"""

    ShopAPIView = {
        "serializer_class": VendorSerializer,
        'GET': {
            'operation_summary': '獲取單一店家訊息',
            'operation_description': '獲取商店靜態訊息__不會有商店狀態，那是在動態訊息__  `會回傳單個vednor arry`',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(
                    'vendor_id',
                    in_=openapi.IN_PATH,
                    description='廠商的`ID`',
                    type=openapi.TYPE_STRING
                )

            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="成功",
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1, description="供應商 `ID`", readOnly=True),
                            'name': openapi.Schema(type=openapi.TYPE_STRING, example="茶壹冷飲", description="供應商名稱"),
                            'email': openapi.Schema(type=openapi.TYPE_STRING, example="yam9668@yahoo.com.tw", description="郵箱地址", format='email'),
                            'contact': openapi.Schema(type=openapi.TYPE_STRING, example="0916233346", description="聯繫方式"),
                            'campus_name': openapi.Schema(type=openapi.TYPE_STRING, example="建功校區", description="校區名稱"),
                            'vendor_img_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="供應商圖片 URL"),
                            'desc': openapi.Schema(type=openapi.TYPE_STRING, example="", description="供應商描述"),
                            'promotions': openapi.Schema(type=openapi.TYPE_STRING, example="", description="促銷信息"),
                            'shop_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="商店 URL"),
                            'ig_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="Instagram URL"),
                            'fd_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="Foodpanda URL"),
                        },
                    ),
                ),
            }

        }

    }

    CurrentStateAPIView = {
        "serializer_class": CurrentStateSerializer,
        'GET': {
            'operation_summary': '獲取商店今日狀態',
            'operation_description': '獲取商店`動態`訊息',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(
                    'vendor_id',
                    in_=openapi.IN_PATH,
                    description='廠商的`ID`',
                    type=openapi.TYPE_STRING,
                    readOnly=True,
                )
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description='成功',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "shopping_type": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description="購物類型",
                                max_length=10,
                                example='online',
                                format="購物類型，應該是 'online' 或 'offline'",
                            ),
                            "date": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                format=openapi.FORMAT_DATE,
                                description="日期，應該是 YYYY-MM-DD 格式的字符串",
                                example=str(date.today()),
                            ),
                            "current_number": openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="當前號碼，應該是正整數",
                                example=0,
                                format="整數",
                            ),
                            "wait_number": openapi.Schema(
                                type=openapi.TYPE_INTEGER,
                                description="等待號碼，應該是正整數",
                                example=0,
                                format="整數",
                            ),
                            "is_start": openapi.Schema(
                                type=openapi.TYPE_BOOLEAN,
                                description="是否開業，應該是布爾值",
                                example=False,
                                format="布爾值",
                            ),
                            "is_delivery_available": openapi.Schema(
                                type=openapi.TYPE_BOOLEAN,
                                description="是否提供外送，應該是布爾值",
                                example=False,
                                format="布爾值",
                            ),
                        }
                    )
                ),


            }
        },
        'PATCH': {
            'operation_summary': '更換商店今日狀態',
            'operation_description': '__今日狀態__ `給ESP32專用` ， 每天伺服器都會做新增狀態',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(
                    'vendor_id',
                    in_=openapi.IN_PATH,
                    description='廠商的__ID__',
                    type=openapi.TYPE_STRING
                )
            ],
            "request_body": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'current_number': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description='現在的號碼'
                    ),
                },
                required=['current_number']
            ),
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description='成功，返回已`更新的號碼`與`ID`',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'vendor_id': openapi.Schema(description='廠商的ID', type=openapi.TYPE_STRING),
                            'current_number': openapi.Schema(type=openapi.TYPE_INTEGER, description='現在的號碼'),
                        },
                        required=['vendor_id', 'current_number']
                    )
                ),
            }

        },

    }

    ShopListAPIView = {
        "serializer_class": VendorSerializer,
        'GET': {
            'operation_summary': '獲取所有店家',
            'operation_description': '獲取商店靜態訊息__不會有商店狀態，那是在動態訊息__  `會回傳多個vednor arry`',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="成功，回多個 `vendor arry`，有做一個小時的緩存配置",
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1, description="供應商 `ID`", readOnly=True),
                            'name': openapi.Schema(type=openapi.TYPE_STRING, example="茶壹冷飲", description="供應商名稱"),
                            'email': openapi.Schema(type=openapi.TYPE_STRING, example="yam9668@yahoo.com.tw", description="郵箱地址", format='email'),
                            'contact': openapi.Schema(type=openapi.TYPE_STRING, example="0916233346", description="聯繫方式"),
                            'campus_name': openapi.Schema(type=openapi.TYPE_STRING, example="建功校區", description="校區名稱"),
                            'vendor_img_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="供應商圖片 URL"),
                            'desc': openapi.Schema(type=openapi.TYPE_STRING, example="", description="供應商描述"),
                            'promotions': openapi.Schema(type=openapi.TYPE_STRING, example="", description="促銷信息"),
                            'shop_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="商店 URL"),
                            'ig_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="Instagram URL"),
                            'fd_url': openapi.Schema(type=openapi.TYPE_STRING, example="null", description="Foodpanda URL"),
                        },
                    ),
                    examples={
                        "application/json":
                            [
                                {
                                    "id": 1,
                                    "name": "茶壹冷飲",
                                    "email": "yam9668@yahoo.com.tw",
                                    "contact": "0916233346",
                                    "campus_name": "建功校區",
                                    "vendor_img_url": None,
                                    "desc": "",
                                    "promotions": "",
                                    "shop_url": None,
                                    "ig_url": None,
                                    "fd_url": None
                                },
                                {
                                    "id": 2,
                                    "name": "唯鎂食棧",
                                    "email": "a0938828252@gmail.com",
                                    "contact": "0908870272",
                                    "campus_name": "建功校區",
                                    "vendor_img_url": "/media/vendor_images/IMG_3234.JPG",
                                    "desc": "",
                                    "promotions": "",
                                    "shop_url": None,
                                    "ig_url": None,
                                    "fd_url": None,
                                }
                            ]
                    },

                ),
            }

        }

    }
