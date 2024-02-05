from django.urls import path, include
from . import views


app_name = "Auth"


urlpatterns = [
    path('get-token/', views.GetTokenAPIView.as_view(), name='get_token'),
]
