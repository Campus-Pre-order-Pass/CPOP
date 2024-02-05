# base import
from helper.base.base_import_view import *

# models
from MenuItem.models import *
from Shop.models import Vendor

# serializers
from MenuItem.serializers import *

from .drf import DRF


# MenuItem =================================================================


@handle_exceptions(MenuItem)
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
class MenuItemAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.MenuItemAPIView["GET"]["operation_summary"],
        operation_description=DRF.MenuItemAPIView["GET"]["operation_description"],
        manual_parameters=DRF.MenuItemAPIView["GET"]["manual_parameters"],
        responses=DRF.MenuItemAPIView["GET"]["responses"],
    )
    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    def get(self, request, vendor_id: int):
        vendor = get_object_or_404(Vendor, id=vendor_id)

        menuItem = MenuItem.objects.filter(vendor=vendor)

        serializer = MenuItemSerializer(menuItem, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, uid):
    #     parser_classes = (MultiPartParser, FormParser)
    #     data = request.data

    #     vendor = Vendor.objects.get(uid=uid)
    #     product_id = uuid.uuid4()
    #     request.data['hot'] = convert_to_bool(request.data['hot'])

    #     menuItem = MenuItem.objects.create(
    #         product_id=product_id,
    #         vendor=vendor,
    #         type=data['type'],
    #         name=data['name'],
    #         price=data['price'],
    #         unit=data['unit'],
    #         desc=data['desc'],
    #         hot=data['hot'],
    #         promotions=data['promotions'],
    #         menu_img_url=f"/static/vendor/{uid}/{product_id}.jpg",
    #     )
    #     if upload_file(request=request, vendor_id=uid, filename=f"{product_id}.jpg"):
    #         menuItem.save()
    #     else:
    #         return Response("upload_file errors", status=status.HTTP_400_BAD_REQUEST)

    #     return Response(status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, uid):
    #     cleaned_product_id = uid.replace("-", "")
    #     menuItem = MenuItem.objects.get(product_id=cleaned_product_id)
    #     serializer = MenuItemSerializer(
    #         menuItem, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, uid):
    #     menuItem = MenuItem.objects.get(uid=uid)
    #     menuItem.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


@handle_exceptions(MenuStatus)
@method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
@method_decorator(base_protection_decorators_v0 , name='dispatch')
class MenuStatusAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.MenuStatusAPIView["GET"]["operation_summary"],
        operation_description=DRF.MenuStatusAPIView["GET"]["operation_description"],
        manual_parameters=DRF.MenuStatusAPIView["GET"]["manual_parameters"],
        responses=DRF.MenuStatusAPIView["GET"]["responses"],
    )
    def get(slef, request, menu_item_id: int):
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)
        serializer = MenuStatusSerializer(
            data=MenuStatus.get_today_status(menu_item=menu_item))
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


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
@method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(base_protection_decorators_v0 , name='dispatch')
class OptionPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.OptionPIView["GET"]["operation_summary"],
        operation_description=DRF.OptionPIView["GET"]["operation_description"],
        manual_parameters=DRF.OptionPIView["GET"]["manual_parameters"],
        responses=DRF.OptionPIView["GET"]["responses"],
    )
    @method_decorator(cache_page(settings.CACHE_TIMEOUT_LONG))
    def get(self, request, menu_id: int):
        """改 int str統一口徑"""
        menuItem = get_object_or_404(MenuItem, id=menu_id)

        data = {
            "extra": (MenuItemExtraOptionSerializer(menuItem).data),
            "required":  (MenuItemRequiredOptionSerializer(menuItem).data)
        }
        return Response(data, status=status.HTTP_200_OK)
