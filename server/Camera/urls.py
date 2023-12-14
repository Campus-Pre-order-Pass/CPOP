from django.urls import path
from .views import *

app_name = "Camera"

urlpatterns = [path("upload_image/", upload_image, name="upload_image")]
