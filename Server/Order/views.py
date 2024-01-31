# django
from django.shortcuts import render
from django.conf import settings
from django.test import TestCase
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
from helper.decorator.custom_ratelimit import custom_ratelimit

# authentication
from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication
from helper.base.base_api_view import BaseAPIViewWithFirebaseAuthentication

# models
from Order.models import Order, OrderItem
from Order.OrderLogic.test.mark import MarkData
from Shop.models import CurrentState, Vendor
from MenuItem.models import MenuItem
from Customer.models import Customer

# order
from Order.OrderLogic.order_logic import OrderLogic

# serializers
from Order.serializers import OrderItemSerializer, OrderSerializer

# helpers
from helper.fileupload import upload_file

# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.vaidate import convert_to_bool


# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache


# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Order.drf import DRF

# trading
from Order.core.trading_system import TradingSystem
from Order.core.module.error.configuration_error import OrderCreationError


# class
trading = TradingSystem(test=settings.TEST)


@handle_exceptions(Order)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
@method_decorator(never_cache, name='get')
@method_decorator(never_cache, name='post')
class PayOrderAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.PayOrderAPIView["GET"]["operation_summary"],
        operation_description=DRF.PayOrderAPIView["GET"]["operation_description"],
        manual_parameters=DRF.PayOrderAPIView["GET"]["manual_parameters"],
        responses=DRF.PayOrderAPIView["GET"]["responses"],
    )
    def get(self, request, uid: str, *args, **kwargs):
        """獲取訂單資訊"""

        c = Customer.objects.get(uid=uid)
        o = Order.objects.filter(customer=c)

        orderSerializer = OrderSerializer(data=o, many=True)
        orderSerializer.is_valid()  # 调用 is_valid() 方法

        return Response({"order": orderSerializer.data})

    @swagger_auto_schema(
        operation_summary=DRF.PayOrderAPIView["POST"]["operation_summary"],
        operation_description=DRF.PayOrderAPIView["POST"]["operation_description"],
        request_body=DRF.PayOrderAPIView["POST"]["request_body"],
        responses=DRF.PayOrderAPIView["POST"]["responses"],
    )
    def post(self, request, uid=None, *args, **kwargs):

        # order_managment = OrderLogic()

        # order_managment.setTest(test=settings.TEST)

        try:
            # Your order logic here
            try:
                # order_managment.check_order(data=request.data)
                trading.setData(data=request.data)
            except OrderCreationError as oce:
                # Handle the ValueError and return an appropriate response
                error_message = str(oce)
                return Response({"error": f"check oredr  in {error_message}", "code": oce.code, "source": oce.error_source}, status=status.HTTP_400_BAD_REQUEST)

            hash_code = trading.execute()

            # Assuming the order creation is successful, return the response
            return Response({"message": "Order created successfully", "hash_code": hash_code}, status=status.HTTP_201_CREATED)

        except OrderCreationError as oce:
            # Handle the ValueError and return an appropriate response
            error_message = str(oce)
            return Response({"error": error_message, "code": oce.code, "source": oce.error_source}, status=status.HTTP_400_BAD_REQUEST)


@handle_exceptions(Order)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
class PayStatusAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.PayStatusAPIView["GET"]["operation_summary"],
        operation_description=DRF.PayStatusAPIView["GET"]["operation_description"],
        responses=DRF.PayStatusAPIView["GET"]["responses"],
    )
    def get(self, request, order_id: int, *args, **kwargs):
        "該訂單目前狀態"
        order = Order.objects.get(id=order_id)
        return Response({"status": order.order_status})


@handle_exceptions(OrderItem)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
class OrderAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.OrderAPIView["GET"]["operation_summary"],
        operation_description=DRF.OrderAPIView["GET"]["operation_description"],
        manual_parameters=DRF.OrderAPIView["GET"]["manual_parameters"],
        responses=DRF.OrderAPIView["GET"]["responses"],
    )
    def get(self, request, uid: str,  order_id: int):
        """
            1. 獲取該訂單的細節
            2. 會有 token
        """
        order = Order.objects.get(id=order_id)
        items = OrderItem.objects.filter(order=order)
        s = OrderItemSerializer(data=items, many=True)
        s.is_valid()

        return Response({"itmes": s.data})
