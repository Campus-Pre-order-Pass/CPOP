# swagger
from drf_yasg import openapi
from typing import Any, Optional, Dict

from rest_framework import serializers


class BaseAPIViewDRFConfig:
    """BaseAPIViewDRFConfig class"""

    FIRE_BASE_HEADER = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Firebase ID Token (Bearer Token)",
        type=openapi.TYPE_STRING,
        required=False,
    )
    # CSRF_BASE_HEADER use in post request ,creat request
    X_CSRF_TOKEN_BASE_HEADER = openapi.Parameter(
        'X-CSRFToken',
        openapi.IN_HEADER,
        description="CSRFToken ID Token. 需要先去 /v0/api/auth/get-token 獲取.....",
        type=openapi.TYPE_STRING,
        required=False,
    )
    TEST_TOKEN_HEADER = openapi.Parameter(
        'test_token',
        openapi.IN_HEADER,
        description="Your test token",
        type=openapi.TYPE_STRING,
        required=False,
    )
    Response = {
        200: openapi.Response("成功"),
        # 201: openapi.Response("新增成功"),
        # 204: openapi.Response("No Content"),
        # 400: openapi.Response("Bad Request"),
        # 401: openapi.Response("Unauthorized"),
        # 403: openapi.Response("Forbidden"),
        404: openapi.Response("Not Found"),
        # 405: openapi.Response("Method Not Allowed"),
        500: openapi.Response("Internal Server Error"),
    }

    @classmethod
    def create_API_DRF_config(cls, serializer_class: serializers.ModelSerializer, methods: any) -> Dict[str, Any]:
        """base `DRF` conf"""
        config = {"serializer_class": serializer_class}

        for method_config in methods:
            # 假设 method_config 是一个字典，代表一个方法的配置
            if isinstance(method_config, dict):
                config.update(method_config)

        return config

    @classmethod
    def creat_request_body(cls, field: str,
                           type: Optional[Any] = None,
                           description: Optional[str] = None) -> openapi.Schema:
        """創造回傳表格"""
        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                field: openapi.Schema(
                    type=type,
                    description=description
                ),
            },
            required=[field]
        )

    @classmethod
    def creat_manual_parameters(cls,
                                field: str,
                                type: Optional[Any] = None,
                                in_: Optional[Any] = None,
                                description: Optional[str] = None) -> openapi.Schema:
        """創造回傳表格"""

        return openapi.Parameter(
            field,
            in_=in_,
            description=description,
            type=type
        )

    @classmethod
    def creat_method_parameters(cls,
                                method: str,
                                operation_summary: Optional[Any],
                                operation_description: Optional[Any],
                                request_body: Optional[Any] = None,
                                manual_parameters: Optional[Any] = None,
                                responses: Optional[Any] = None) -> dict[Any]:
        """基本abse conf"""
        return {
            method: {
                'operation_summary': operation_summary,
                'operation_description': operation_description,
                'manual_parameters': manual_parameters,
                "request_body": request_body,
                "responses": responses if responses else cls.Response,
            }
        }
