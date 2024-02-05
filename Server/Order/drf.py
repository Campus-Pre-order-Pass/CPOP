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
from Order.serializers import OrderItemSerializer, OrderRequestBodySerializer, OrderSerializer
from rest_framework.views import APIView

description = """
# 错误代码（Error Code）

以下是一些错误代码及其相应的解释。

## OK
- `SUCESS_CODE` (Success Code): 200

## 格式错误
- `FORMAT_ERROR`: 303

## 模型错误
- `MODELS_ERROR`: 307
- `MODELS_NOT_FOUND`: 308

## 新增与订单验证相关的错误码
- `VAILD_ERROR` (Validation Error): 399
- `BUSINESS_HOURS_ERROR`: 400
- `INVENTORY_ERROR`: 401
- `USER_PURCHASE_LIMIT_ERROR`: 402
- `DAILY_PURCHASE_LIMIT_ERROR`: 403

## 厂商条件错误
- `VENDOR_VAILD_ERROR`: 606

## 一般错误
- `ERROR_CODE`: 500

## 用户设置
- `MAX_USER_PURCHASE_LIMIT`: 2

## 其他设置
- `NOT_POSIT_ERROR`: 501

## 打印错误
- `PRINTER_ERROR`: 502

"""
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

    PayOrderAPIView = {
        "serializer_class": OrderItemSerializer,
        'GET': {
            'operation_summary': '獲取訂單訊息',
            'operation_description': '獲取`所有`顧客訂單消息`只有價格....` ',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                uid_param
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="成功 回傳 order `Order ARRY`",
                    examples={
                        "application/json": [
                         {
                             "order": [
                                 {
                                     "id": 1,
                                     "order_time": "2023-12-29T16:15:19.711723",
                                     "take_time": "2023-12-29T16:15:19.711729",
                                     "total_amount": "425.00",
                                     "order_status": "created",
                                     "confirmation_hash": "84ecd52d71cfbc1b89aa1e9a364f8c08b07db5d1dcdb5cc5a543b26634096c7f",
                                     "vendor": 1,
                                     "customer": 1
                                 },
                                 {
                                     "id": 2,
                                     "order_time": "2023-12-29T16:16:36.025166",
                                     "take_time": "2023-12-29T16:16:36.025184",
                                     "total_amount": "425.00",
                                     "order_status": "created",
                                     "confirmation_hash": "684abee3b9b4f783b2ec0512cda4f63f2a69cebce4c148807f175c14412e1f89",
                                     "vendor": 1,
                                     "customer": 1
                                 },
                             ]
                         }
                        ]
                    },
                    schema=OrderSerializer(many=True),
                ),
            },
        },
        'POST': {
            'operation_summary': '新增訂單',
            'operation_description': '**重要** 透過此api完成`訂單動作`',
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                BaseAPIViewDRFConfig.X_CSRF_TOKEN_BASE_HEADER,
                uid_param,
            ],
            "request_body": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'vendor_id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1, description="供應商 `ID`"),
                    'take_time': openapi.Schema(type=openapi.TYPE_STRING, example="2022-02-01T12:34:56", description="取貨時間`"),
                    'uid': openapi.Schema(type=openapi.TYPE_STRING, example="test", description="顧客 `ID`"),
                    'order_items': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'menu_item_id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1, description="菜單項目 `ID`"),
                                'required_option_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), example=[1, 2], description="必選選項 `ID`"),
                                'extra_option_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), example=[1, 2], description="額外選項 `ID`"),
                                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, example=2, description="數量"),
                            }

                        ),
                        example={
                            "vendor_id": 1,
                            "uid": "test",
                            "take_time": "2022-02-01T12:34:56",
                            "order_items": [
                                {
                                    "menu_item_id": 36,
                                    "required_option_ids": [
                                        1,
                                        2
                                    ],
                                    "extra_option_ids": [
                                        1,
                                        2
                                    ],
                                    "quantity": 4
                                },
                                {
                                    "menu_item_id": 2,
                                    "required_option_ids": [
                                        3,
                                        4
                                    ],
                                    "extra_option_ids": [
                                        3,
                                        4
                                    ],
                                    "quantity": 3
                                }
                            ]
                        }
                    ),
                },
                description="訂單請求的 `JSON` 格式",
            ),
            "responses": {
                status.HTTP_201_CREATED: openapi.Response(
                    description='成功，返回已是成功，只要是 `201`以外的都算是錯誤',
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                                'message': openapi.Schema(type=openapi.TYPE_STRING, description="回傳成功訊息", example="Order created successfully"),
                                'hash_code': openapi.Schema(type=openapi.TYPE_STRING, description="該訂單的hash值", example="rdfayvghsbdjnmjasnkmdsal;kd156tghin31"),
                        }

                    ),
                ),

                status.HTTP_400_BAD_REQUEST: openapi.Response(
                    description=description,
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'code': openapi.Schema(type=openapi.TYPE_INTEGER, description="回傳錯誤代碼", example=999),
                            'message': openapi.Schema(type=openapi.TYPE_STRING, description="回傳錯誤訊息", example="this is a error message"),
                            'source': openapi.Schema(type=openapi.TYPE_STRING, description="回傳錯誤", example="on Order.trad.example()..."),
                        }

                    ),
                ),



            }
        }

    }

    PayStatusAPIView = {
        "GET": {
            "operation_summary": "獲取訂狀態",
            "operation_description": "獲取訂狀態，像是 `處理中`...",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER
            ],
            "responses": {
                status.HTTP_200_OK: openapi.Response(
                    description="成功獲取",
                    schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "order_status": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                example="process",
                                description="訂單處理狀態"
                            ),
                        },
                    ),
                ),
            },

        }

    }

    OrderAPIView = {
        "GET": {
            "operation_summary": "獲取該訂單細節",
            "operation_description": "像是點了什麼之類的",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
                uid_param
            ],
            "responses": {
                status.HTTP_200_OK: OrderItemSerializer(many=True)
            }
        }
    }
