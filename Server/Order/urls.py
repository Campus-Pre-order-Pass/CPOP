from django.urls import path
from . import views

app_name = "Order"

urlpatterns = [
    # 建立訂單
    #     path('pay/create/<int:customer_id>',
    #          views.PayOrderAPIView.as_view(), name='create_order'),

    # 查看訂單狀態
    path('pay/status/<int:order_id>',
         views.PayStatusAPIView.as_view(), name='order_status'),

    # 查看過往訂單
    path('item/<str:uid>/<int:order_id>',
         views.OrderAPIView.as_view(), name='view_orders'),

    # 下訂單
    path('pay/<str:uid>',
         views.PayOrderAPIView.as_view(), name='pay_order'),

    #     path('pay',
    #          views.PayOrderAPIView.as_view(), name='pay_order'),
]
