from django.urls import path
from . import views

app_name = "Order"

urlpatterns = [
    # 建立訂單
    path('pay', views.PayOrderAPIView.as_view(), name='create_order'),
    path('pay/status', views.PayStatusAPIView.as_view(), name='order_status'),

    # 查看過往訂單
    path('orders', views.OrderAPIView.as_view(), name='view_orders'),
]
