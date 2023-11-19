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
from MenuItem.models import MenuItem, MenuStatus, ExtraOption, RequiredOption
from Shop.models import Vendor


# serializers
from MenuItem.serializers import MenuItemExtraOptionSerializer, MenuItemRequiredOptionSerializer, MenuItemSerializer, ExtraOptionSerializer, RequiredOptionSerializer

# helpers
from helper.fileupload import upload_file

# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.vaidate import convert_to_bool


# cache
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control

# MenuItem =================================================================


@handle_exceptions(MenuItem)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class MenuItemAPIView(APIView):
    renderer_classes = [JSONRenderer]

    # TODO: 是 DEBUG
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 在这里进行条件判断并设置属性
        if not settings.DEBUG:
            self.authentication_classes = [FirebaseTokenAuthentication]

    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    def get(self, request, uid):
        vendor = Vendor.objects.get(id=uid)

        menuItem = MenuItem.objects.filter(vendor=vendor)

        serializer = MenuItemSerializer(menuItem, many=True)
        return Response(serializer.data)

    def post(self, request, uid):
        parser_classes = (MultiPartParser, FormParser)
        data = request.data

        vendor = Vendor.objects.get(uid=uid)
        product_id = uuid.uuid4()
        request.data['hot'] = convert_to_bool(request.data['hot'])

        menuItem = MenuItem.objects.create(
            product_id=product_id,
            vendor=vendor,
            type=data['type'],
            name=data['name'],
            price=data['price'],
            unit=data['unit'],
            desc=data['desc'],
            hot=data['hot'],
            promotions=data['promotions'],
            menu_img_url=f"/static/vendor/{uid}/{product_id}.jpg",
        )
        if upload_file(request=request, vendor_id=uid, filename=f"{product_id}.jpg"):
            menuItem.save()
        else:
            return Response("upload_file errors", status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, uid):
        cleaned_product_id = uid.replace("-", "")
        menuItem = MenuItem.objects.get(product_id=cleaned_product_id)
        serializer = MenuItemSerializer(
            menuItem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid):
        menuItem = MenuItem.objects.get(uid=uid)
        menuItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @handle_exceptions(ExtraOption)
# # @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# # @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# # @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
# class ExtraOptionPIView(APIView):

#     # TODO: 是 DEBUG
#     if not settings.DEBUG:
#         authentication_classes = [FirebaseTokenAuthentication]
#     renderer_classes = [JSONRenderer]

#     def get(self, request, menu_id):
#         """改 int str統一口徑"""
#         menuItem = MenuItem.objects.get(id=int(menu_id))

#         serializer = MenuItemExtraOptionSerializer(menuItem)
#         return Response(serializer.data)

@handle_exceptions(MenuItem)
class OptionPIView(APIView):
    renderer_classes = [JSONRenderer]

    # TODO: 是 DEBUG
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 在这里进行条件判断并设置属性
        if not settings.DEBUG:
            self.authentication_classes = [FirebaseTokenAuthentication]

    # @cache_page(settings.CACHE_TIMEOUT_LONG)
    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    def get(self, request, menu_id):
        """改 int str統一口徑"""
        menuItem = MenuItem.objects.get(id=int(menu_id))

        data = {
            "extra": (MenuItemExtraOptionSerializer(menuItem).data),
            "required":  (MenuItemRequiredOptionSerializer(menuItem).data)
        }
        return Response(data)
