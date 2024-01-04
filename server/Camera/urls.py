from django.urls import path
from . import views

app_name = "Camera"

urlpatterns = [
    path("upload_image/", views.UploadImageAPIView.as_view(), name="upload_image")]
