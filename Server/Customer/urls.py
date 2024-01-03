from django.urls import path, include
from . import views


app_name = "Auth"


urlpatterns = [
    # customer
    path('<str:uid>', views.CustomerAPIView.as_view(),
         name="CustomerAPIView"),
    path('', views.CustomerAPIView.as_view(),
         name="CustomerAPIView"),
]
