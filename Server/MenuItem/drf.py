# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# rest_framework
from rest_framework import status

# MarkData
from Order.OrderLogic.test.mark import MarkData

# BaseAPIViewDRFConfig
from helper.base.drf_yasg_base import BaseAPIViewDRFConfig

# serializers
from Order.serializers import *
from MenuItem.serializers import *
from rest_framework.views import APIView

menu_id = openapi.Parameter(
    name="menu_id",
    in_=openapi.IN_PATH,
    type=openapi.TYPE_INTEGER,
    description="菜單 ID",
    required=True,
    example=1,
),


class DRF(APIView):
    """drf_yasg app configuration"""

    OptionPIView = {
        "GET": {
            "operation_summary": "獲取額外選項與必選選項",
            "operation_description": "獲取該菜單的個種選項，像是`荷包蛋....`",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(
                    name="menu_id",
                    in_=openapi.IN_PATH,
                    type=openapi.TYPE_INTEGER,
                    description="菜單 ID",
                    required=True,
                    example=1,
                ),
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="成功獲取，回傳`extra`跟`required`",
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "extra": openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                description="額外選項",
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "id": openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description="額外選項 ID",
                                            example=1,
                                        ),
                                        "name": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="額外選項名稱",
                                            example="荷包蛋",
                                        ),
                                        "description": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="額外選項描述",
                                            example="加一顆荷包蛋",
                                        ),
                                        "price": openapi.Schema(
                                            type=openapi.TYPE_NUMBER,
                                            description="額外選項價格",
                                            example=5.99,
                                        ),
                                    },
                                ),),
                            "required": openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                description="必選選項",
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "id": openapi.Schema(
                                            type=openapi.TYPE_INTEGER,
                                            description="額外選項 ID",
                                            example=1,
                                        ),
                                        "name": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="額外選項名稱",
                                            example="荷包蛋",
                                        ),
                                        "description": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="額外選項描述",
                                            example="加一顆荷包蛋",
                                        ),
                                        "price": openapi.Schema(
                                            type=openapi.TYPE_NUMBER,
                                            description="額外選項價格",
                                            example=5.99,
                                        ),
                                    },
                                ),),
                        },
                    ),
                ),
            }
        }

    }

    MenuItemAPIView = {
        "GET": {
            "operation_summary": "獲取菜單",
            "operation_description": "獲取該廠商的菜單",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(name="vendor_id", type=openapi.TYPE_INTEGER, in_=openapi.IN_PATH,
                                  example=1, description="供應商 `ID`"),

            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="回傳 `MenuItem arry`",
                    schema=MenuItemSerializer(many=True),
                    examples={
                        "application/json":
                        [
                            {
                                "id": 1,
                                "category": [
                                    "鮮泡茶飲"
                                ],
                                "title": "茉香綠茶",
                                "price": "30.00",
                                "unit": "杯",
                                "hot": False,
                                "menu_img_url": "/media/menu_images/%E9%AE%AE%E6%B3%A1%E8%8C%B6%E9%A3%B2.jpeg",
                                "desc": "",
                                "promotions": None,
                                "daily_max_orders": 100,
                                "remaining_quantity": 20
                            },
                            {
                                "id": 2,
                                "category": [
                                    "鮮泡茶飲"
                                ],
                                "title": "台灣青茶",
                                "price": "30.00",
                                "unit": "杯",
                                "hot": False,
                                "menu_img_url": "/media/menu_images/%E9%AE%AE%E6%B3%A1%E8%8C%B6%E9%A3%B2_CertnnH.jpeg",
                                "desc": "",
                                "promotions": None,
                                "daily_max_orders": 100,
                                "remaining_quantity": 20
                            },
                            {
                                "id": 3,
                                "category": [
                                    "鮮泡茶飲"
                                ],
                                "title": "金萱烏龍茶",
                                "price": "35.00",
                                "unit": "杯",
                                "hot": False,
                                "menu_img_url": "/media/menu_images/%E9%AE%AE%E6%B3%A1%E8%8C%B6%E9%A3%B2_2jFJFjW.jpeg",
                                "desc": "",
                                "promotions": None,
                                "daily_max_orders": 100,
                                "remaining_quantity": 20
                            },
                        ]
                    }

                )
            }
        }
    }
    MenuStatusAPIView = {
        "GET": {
            "operation_summary": "獲取該菜單品項狀態",
            "operation_description": "像是 水餃店的水餃品項只剩下5份`",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                openapi.Parameter(
                    name="menu_item_id",
                    in_=openapi.IN_PATH,
                    type=openapi.TYPE_INTEGER,
                    description="該菜單的`ID`",
                    required=True,
                    example=1,
                ),
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="回傳該 status",
                    schema=MenuStatusSerializer(),
                    examples={
                        "application/json": {
                                "preorder_qty": 1,
                            "remaining_quantity": 2,
                            "is_available": True

                        },


                    }
                )
            }

        }
    }
