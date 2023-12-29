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

from Order.OrderLogic.error.error import OrderCreationError


# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache

# customer order history =================================================


@handle_exceptions(Order)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
@method_decorator(never_cache, name='post')
class PayOrderAPIView(APIView):
    def get(self, request, customer_id: int):
        """獲取訂單資訊"""
        c = Customer.objects.get(id=customer_id)
        o = Order.objects.filter(customer=c)

        orderSerializer = OrderSerializer(data=o, many=True)
        orderSerializer.is_valid()  # 调用 is_valid() 方法

        # 如果验证成功，可以访问 orderSerializer.data 或 orderSerializer.validated_data
        # print(orderSerializer.data)

        return Response({"order": orderSerializer.data})

    def post(self, request,  customer_id: int = None):
        "新增訂單資訊"

        order_managment = OrderLogic()

        order_managment.setTest(settings.TEST)

        try:
            # Your order logic here
            order_managment.check_order(request.data)
            hash_code = order_managment.order()

            # Assuming the order creation is successful, return the response
            return Response({"message": "Order created successfully", "hash_code": hash_code}, status=status.HTTP_201_CREATED)

        except OrderCreationError as oce:
            # Handle the ValueError and return an appropriate response
            error_message = str(oce)
            return Response({"error": error_message, "code": oce.code, "source": oce.error_source}, status=status.HTTP_400_BAD_REQUEST)


@handle_exceptions(Order)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
class PayStatusAPIView(APIView):
    def get(self, request, order_id: int, *args, **kwargs):
        "該訂單目前狀態"
        order = Order.objects.get(id=order_id)
        return Response({"status": order.order_status})


@handle_exceptions(OrderItem)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
class OrderAPIView(APIView):
    def get(self, request, order_id: int):
        """
            1. 獲取該訂單的細節
            2. 會有 token
        """
        order = Order.objects.get(id=order_id)
        items = OrderItem.objects.filter(order=order)
        s = OrderItemSerializer(data=items, many=True)
        s.is_valid()

        return Response({"itmes":   s.data})
