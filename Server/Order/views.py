# base import 
from helper.base.base_import_view import *

# django 
from django.db import transaction
from django.middleware import csrf
from django.contrib.auth.decorators import login_required

# models
from Order.models import Order, OrderItem
from Customer.models import Customer

# serializers
from Order.serializers import *

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
@method_decorator(base_protection_decorators_v0 , name='dispatch')
# @method_decorator(user_passes_test_404(is_whitelisted) , name='dispatch')
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
    # @transaction.atomic   # 滾回資料
    # @csrf_protect         # CSRF保護
    # @ensure_csrf_cookie   # 這個裝飾器確保 CSRF 標記（token）包含在 HTTP 響應的 cookie 中。
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
@method_decorator(base_protection_decorators_v0 , name='dispatch')
class PayStatusAPIView(BaseAPIViewWithFirebaseAuthentication):
    @swagger_auto_schema(
        operation_summary=DRF.PayStatusAPIView["GET"]["operation_summary"],
        operation_description=DRF.PayStatusAPIView["GET"]["operation_description"],
        responses=DRF.PayStatusAPIView["GET"]["responses"],
    )
    def get(self, request, order_id: int, *args, **kwargs):
        "該訂單目前狀態"
        order = get_object_or_404(Order, id=order)
        return Response({"status": order.order_status})


@handle_exceptions(OrderItem)
@method_decorator(custom_ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='GET'), name='get')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='POST'), name='post')
# @method_decorator(ratelimit(key='ip', rate=settings.RATELIMITS_USER, method='DELETE'), name='delete')
@method_decorator(never_cache, name='get')
@method_decorator(base_protection_decorators_v0 , name='dispatch')
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
        order = get_object_or_404(Order, id=order)
        items = OrderItem.objects.filter(order=order)
        s = OrderItemSerializer(data=items, many=True)
        s.is_valid()

        return Response({"itmes": s.data})




