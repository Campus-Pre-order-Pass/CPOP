from django.urls import path, include
from . import views


app_name = "Auth"


urlpatterns = [
    # vendor
    path('vendor/<str:uid>', views.VendorAPIView.as_view(), name="VendorAPIView"),

    # customer
    path('customer/<str:uid>', views.CustomerAPIView.as_view(),
         name="CustomerAPIView"),
]
