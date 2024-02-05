# django
from django.shortcuts import render
from django.conf import settings
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
import os
import uuid

# rest_framework
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# rate
from django_ratelimit.decorators import ratelimit

# authentication
from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication
from Customer.models import Customer
from helper.base.base_api_view import BaseAPIViewWithFirebaseAuthentication
from Shop.models import CurrentState, Vendor
from Customer.serializers import CustomerSerializerSerializer

# models

# from Shop.models.shop import Shop


# serializers
from Shop.serializers import VendorSerializer


# helpers
from helper.fileupload import upload_file

# handle_exceptions
from helper.handle_exceptions import handle_exceptions


# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache


from helper.decorator.custom_ratelimit import custom_ratelimit
from helper.decorator.base import base_protection_decorators_v0


# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .drf import DRF

# ----------------------------------------------------------------


@handle_exceptions(Customer)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='PATCH'), name='dispatch')
@method_decorator(never_cache, name='dispatch')
@method_decorator(base_protection_decorators_v0 , name='dispatch')
class CustomerAPIView(BaseAPIViewWithFirebaseAuthentication):
    """有關顧客的api view"""

    @swagger_auto_schema(
        operation_summary=DRF.CustomerAPIView["GET"]["operation_summary"],
        operation_description=DRF.CustomerAPIView["GET"]["operation_description"],
        manual_parameters=DRF.CustomerAPIView["GET"]["manual_parameters"],
        responses=DRF.CustomerAPIView["GET"]["responses"],
    )
    def get(self, request, uid: str):
        c = Customer.objects.get(uid=uid)
        serializer = CustomerSerializerSerializer(c)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary=DRF.CustomerAPIView["POST"]["operation_summary"],
        operation_description=DRF.CustomerAPIView["POST"]["operation_description"],
        manual_parameters=DRF.CustomerAPIView["POST"]["manual_parameters"],
        request_body=DRF.CustomerAPIView["POST"]["request_body"],
        responses=DRF.CustomerAPIView["POST"]["responses"],
    )
    def post(self, request, uid: str, *args, **kwargs):
        serializer = CustomerSerializerSerializer(data=request.data)

        # 检查数据是否有效
        if serializer.is_valid():
            # 数据格式正确，可以继续处理
            c = Customer.objects.create(**serializer.validated_data)
            c.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 数据格式不正确，返回错误响应
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary=DRF.CustomerAPIView["PATCH"]["operation_summary"],
        operation_description=DRF.CustomerAPIView["PATCH"]["operation_description"],
        manual_parameters=DRF.CustomerAPIView["PATCH"]["manual_parameters"],
        request_body=DRF.CustomerAPIView["PATCH"]["request_body"],
        responses=DRF.CustomerAPIView["PATCH"]["responses"],
    )
    def patch(self, request, uid: str):
        c = Customer.objects.get(uid=uid)
        serializer = CustomerSerializerSerializer(
            c, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @swagger_auto_schema(
    #     operation_summary=DRF.CustomerAPIView["DELETE"]["operation_summary"],
    #     operation_description=DRF.CustomerAPIView["DELETE"]["operation_description"],
    #     manual_parameters=DRF.CustomerAPIView["DELETE"]["manual_parameters"],
    #     responses=DRF.CustomerAPIView["DELETE"]["responses"],
    # )
    # def delete(self, request, uid: str):
    #     c = Customer.objects.get(uid=uid)
    #     c.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
