from django.urls import path, include
from . import views


app_name = "Shop"


urlpatterns = [

    # current
    path('current/<int:vendor_id>',
         views.CurrentStateAPIView.as_view(), name="current"),

    # file
    # path('file/<str:uid>', views.update_image, name="update_image"),

    # shop
    path('<int:vendor_id>', views.ShopAPIView.as_view(), name="shop"),

    # shop_list
    path('', views.ShopListAPIView.as_view(), name="shop_list"),
]
