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
from Shop.models import CurrentState, Vendor
from MenuItem.models import MenuItem

# order
from Order.OrderLogic.order_logic import OrderLogic

# serializers

# helpers
from helper.fileupload import upload_file

# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.vaidate import convert_to_bool


# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.cache import cache_control

# customer order history =================================================


# @handle_exceptions(Vendor)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class PayOrderAPIView(APIView):
    def get(self, request):
        """獲取訂單資訊"""

        OrderLogic.create_order(request.data)
        OrderLogic.order()

        orders = [{'order_id': 1, 'status': 'pending', 'amount': 50.00},
                  {'order_id': 2, 'status': 'completed', 'amount': 75.00}]

        return Response({'orders': orders}, status=status.HTTP_200_OK)

    def post(self, request):
        "新增訂單資訊"
        # 处理创建订单的逻辑，例如从请求中获取订单信息并保存到数据库
        # 这里只是一个示例，你需要根据实际情况来编写具体的逻辑
        data = request.data
        # 根据请求中的数据创建订单
        # ...

        return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)


# @handle_exceptions(Vendor)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')


class PayStatusAPIView(APIView):
    pass


# @handle_exceptions(Vendor)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class OrderAPIView(APIView):
    pass
