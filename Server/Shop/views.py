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
from helper.decorator.custom_ratelimit import custom_ratelimit

# DRF
from Shop.drf import DRF

# authentication
from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication
from helper.base.base_api_view import BaseAPIViewWithFirebaseAuthentication
from Shop.models import CurrentState, Vendor
from MenuItem.models import MenuItem

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
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache

# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# other packages
from rest_framework.generics import GenericAPIView


# shop =================================================================

@handle_exceptions(Vendor)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
class ShopAPIView(BaseAPIViewWithFirebaseAuthentication):
    # to Swagger
    # serializer_class = DRF.ShopAPIView["serializer_class"]

    # @swagger_auto_schema(
    #     operation_summary=DRF.ShopAPIView["GET"]["operation_summary"],
    #     manual_parameters=DRF.ShopAPIView["GET"]["manual_parameters"]
    # )

    @swagger_auto_schema(
        operation_summary=DRF.ShopAPIView["GET"]["operation_summary"],
        operation_description=DRF.ShopAPIView["GET"]["operation_description"],
        manual_parameters=DRF.ShopAPIView["GET"]["manual_parameters"],
        responses=DRF.ShopAPIView["GET"]["responses"],
    )
    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    def get(self, request, vendor_id=None):
        # TODO: 要加入校區判斷

        # TODO: 需要做 cache views seperator
        shop_list = []

        if vendor_id:
            # 处理特定shop_id的情况

            vendor = Vendor.objects.get(id=vendor_id)
            # current_state = CurrentState.get_today_status(
            #     vendor_id=int(shop_id))

            vendor_serializer = VendorSerializer(vendor)
            # current_state_serializer = CurrentStateSerializer(
            #     current_state)

            shop_list = {
                "vendor": vendor_serializer.data,
                # "current": current_state_serializer.data
            }

        else:
            # 处理没有提供shop_id的情况
            vendor_list = Vendor.objects.all()

            for vendor in vendor_list:
                # try:
                #     current_state = CurrentState.get_today_status(
                #         vendor_id=int(shop_id))
                # except CurrentState.DoesNotExist:
                #     # Handle the case where there is no CurrentState for the vendor.
                #     current_state = None

                vendor_serializer = VendorSerializer(vendor)
                # current_state_serializer = CurrentStateSerializer(
                #     current_state) if current_state else None

                shop_list.append({
                    "vendor": vendor_serializer.data,
                    # "current": current_state_serializer.data if current_state_serializer else None
                })

                # shop_list.append(vendor_serializer)

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
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='PATCH'), name='patch')
@method_decorator(never_cache, name='get')
class CurrentStateAPIView(BaseAPIViewWithFirebaseAuthentication):
    # to Swagger
    # serializer_class = DRF.CurrentStateAPIView["serializer_class"]

    @swagger_auto_schema(
        operation_summary=DRF.CurrentStateAPIView["GET"]["operation_summary"],
        operation_description=DRF.CurrentStateAPIView["GET"]["operation_description"],
        manual_parameters=DRF.CurrentStateAPIView["GET"]["manual_parameters"],
        responses=DRF.CurrentStateAPIView["GET"]["responses"],
    )
    def get(self, request, vendor_id: str):
        # v = Vendor.objects.get(id=int(vendor_id))
        # serializer = CurrentStateSerializer(CurrentState.objects.get(vendor=v))
        serializer = CurrentStateSerializer(
            CurrentState.get_today_status(vendor_id=int(vendor_id)))
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary=DRF.CurrentStateAPIView["PATCH"]["operation_summary"],
        operation_description=DRF.CurrentStateAPIView["PATCH"]["operation_description"],
        manual_parameters=DRF.CurrentStateAPIView["PATCH"]["manual_parameters"],
        request_body=DRF.CurrentStateAPIView["PATCH"]["request_body"],
        responses=DRF.CurrentStateAPIView["PATCH"]["responses"],
    )
    def patch(self, request, vendor_id: str):
        c = CurrentState.get_today_status(vendor_id=int(vendor_id))
        serializer = CurrentStateSerializer(
            c, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @swagger_auto_schema(
#     deprecated=True
# )
# def upload_vendor_image(request, vendor_id: str):
#     if request.method == 'POST':
#         vendor = Vendor.objects.get(pk=vendor_id)
#         image = request.FILES['image']  # 从表单中获取图像文件
#         vendor.vendor_img_url = image  # 将图像存储到模型的图像字段中
#         vendor.save()


@handle_exceptions(Vendor)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
class ShopListAPIView(BaseAPIViewWithFirebaseAuthentication):
    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    @swagger_auto_schema(
        operation_summary=DRF.ShopListAPIView["GET"]["operation_summary"],
        operation_description=DRF.ShopListAPIView["GET"]["operation_description"],
        manual_parameters=DRF.ShopListAPIView["GET"]["manual_parameters"],
        responses=DRF.ShopListAPIView["GET"]["responses"],
    )
    def get(slef, request, *args, **kwargs):
        v = Vendor.objects.all()
        vendor_serializer = VendorSerializer(v, many=True)

        return Response(vendor_serializer.data, status=status.HTTP_200_OK)
