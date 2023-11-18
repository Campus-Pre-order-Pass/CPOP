from django.urls import path, include
from . import views


app_name = "Shop"


urlpatterns = [

    # current
    path('current/<str:uid>', views.CurrentStateAPIView.as_view(), name="current"),

    # file
    path('file/<str:uid>', views.update_image, name="update_image"),

    # shop
    path('<str:shop_id>', views.ShopAPIView.as_view(), name="shop"),
    path('', views.ShopAPIView.as_view(), name="shop"),
]
