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

# models


# serializers
from Shop.serializers import CurrentStateSerializer, VendorSerializer
from MenuItem.serializers import MenuItemSerializer

# helpers
from helper.fileupload import upload_file

# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.vaidate import convert_to_bool


# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def check_redis_connection():
    try:
        # 嘗試從 Redis 中獲取一個不存在的鍵，此操作不會修改 Redis 中的數據
        cache.get('nonexistent_key_for_connection_check')
        print("Redis connection is active.")
    except Exception as e:
        print(f"Error connecting to Redis: {e}")


# 執行檢查
check_redis_connection()


# shop =================================================================

@handle_exceptions(Vendor)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class ShopAPIView(APIView):

    @cache_page(settings.CACHE_TIMEOUT_LONG)
    def get(self, request, shop_id=None):

        # TODO: 要加入校區判斷
        shop_list = []

        if shop_id:
            # 处理特定shop_id的情况
            try:
                vendor = Vendor.objects.get(id=shop_id)
                current_state = CurrentState.objects.get(vendor=vendor)

                vendor_serializer = VendorSerializer(vendor)
                current_state_serializer = CurrentStateSerializer(
                    current_state)

                shop_list = {
                    "vendor": vendor_serializer.data,
                    "current": current_state_serializer.data
                }
            except (Vendor.DoesNotExist, CurrentState.DoesNotExist):
                # 处理未找到供应商或当前状态的情况
                shop_list = {}
        else:
            # 处理没有提供shop_id的情况
            vendor_list = Vendor.objects.all()

            for vendor in vendor_list:
                try:
                    current_state = CurrentState.objects.get(vendor=vendor)
                except CurrentState.DoesNotExist:
                    # Handle the case where there is no CurrentState for the vendor.
                    current_state = None

                vendor_serializer = VendorSerializer(vendor)
                current_state_serializer = CurrentStateSerializer(
                    current_state) if current_state else None

                shop_list.append({
                    "vendor": vendor_serializer.data,
                    "current": current_state_serializer.data if current_state_serializer else None
                })

        return Response(shop_list)


# MenuItem =================================================================


@api_view(["PUT"])
def update_image(request, uid):
    try:
        cleaned_product_id = uid.replace("-", "")
        menuItem = MenuItem.objects.get(product_id=cleaned_product_id)

        upload_file(request=request, vendor_id=uid, filename=f"{uid}.jpg")
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@handle_exceptions(CurrentState)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class CurrentStateAPIView(APIView):
    if not settings.DEBUG:
        authentication_classes = [FirebaseTokenAuthentication]
    renderer_classes = [JSONRenderer]

    def get(self, request, uid):
        v = Vendor.objects.get(uid=uid)
        serializer = CurrentStateSerializer(CurrentState.objects.get(vendor=v))
        return Response(serializer.data)

    def put(self, request, uid):
        v = Vendor.objects.get(uid=uid)
        c = CurrentState.objects.get(vendor=v)
        serializer = CurrentStateSerializer(
            c, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def upload_vendor_image(request, vendor_id):
    if request.method == 'POST':
        vendor = Vendor.objects.get(pk=vendor_id)
        image = request.FILES['image']  # 从表单中获取图像文件
        vendor.vendor_img_url = image  # 将图像存储到模型的图像字段中
        vendor.save()