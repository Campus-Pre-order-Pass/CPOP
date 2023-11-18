from django.urls import path, include
from . import views


app_name = "MenuItem"


urlpatterns = [
    # menu


    path('options/<str:menu_id>', views.OptionPIView.as_view(),
         name="ExtraOptionPIView"),

    path('<str:uid>', views.MenuItemAPIView.as_view(), name="VendorAPIView"),
]
