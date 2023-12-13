from django.urls import path
from .views import *

urlpatterns = [path("upload_image/", upload_image, name="upload_image")]
