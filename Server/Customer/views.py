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
# from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication
from Customer.models import Customer
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


# ----------------------------------------------------------------


@handle_exceptions(Customer)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class CustomerAPIView(APIView):
    """有關顧客的api view"""
    if not settings.DEBUG:
        authentication_classes = [FirebaseTokenAuthentication]
    renderer_classes = [JSONRenderer]  # 设置渲染器

    def get(self, request, uid):
        c = Customer.objects.get(uid=uid)
        serializer = CustomerSerializerSerializer(c)

        return Response(serializer.data)

    def post(self, request, uid):
        serializer = CustomerSerializerSerializer(data=request.data)

        # 检查数据是否有效
        if serializer.is_valid():
            # 数据格式正确，可以继续处理
            vendor = Customer.objects.create(**serializer.validated_data)
            vendor.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            # 数据格式不正确，返回错误响应
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, uid):
        cleaned_uid = uid.replace("-", "")
        vendor = Customer.objects.get(uid=cleaned_uid)
        serializer = CustomerSerializerSerializer(
            vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid):
        c = Customer.objects.get(uid=uid)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
