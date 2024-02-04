from django.urls import path, include
from . import views


app_name = "MenuItem"


urlpatterns = [
    # menu

    path('options/<str:menu_id>', views.OptionPIView.as_view(),
         name="ExtraOptionPIView"),
    # path('test', views.test, name="TestOptionPIView"),
    path('<int:vendor_id>', views.MenuItemAPIView.as_view(), name="VendorAPIView"),
    path('status/<int:menu_item_id>', views.MenuStatusAPIView.as_view(),
         name="MenuStatusAPIView"),
]
