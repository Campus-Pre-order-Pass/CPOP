# is auto generated
# --django
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.conf import settings
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test , permission_required

import uuid
import os

# rest_framework
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# other packages
from rest_framework.generics import GenericAPIView


# --rate
from django_ratelimit.decorators import ratelimit

# authentication
from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication


# --cache
from django.views.decorators.cache import cache_page
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache


# --swagger
from drf_yasg.utils import swagger_auto_schema

# --helpers

# BaseAPIViewWithFirebaseAuthentication
from helper.base.base_api_view import BaseAPIViewWithFirebaseAuthentication


# handle_exceptions
from helper.handle_exceptions import handle_exceptions
from helper.vaidate import convert_to_bool
from helper.fileupload import upload_file


# custom_ratelimit
from helper.decorator.custom_ratelimit import custom_ratelimit
from helper.decorator.base import *
from helper.auth.group import *