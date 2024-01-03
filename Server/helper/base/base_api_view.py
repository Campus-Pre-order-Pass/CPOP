# django
from django.shortcuts import render
from django.conf import settings
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
import os
import uuid

# rest_framework
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# rate
from django_ratelimit.decorators import ratelimit

# authentication
from Auth.Authentication.authentication import FirebaseAuthentication, FirebaseTokenAuthentication


class BaseAPIViewWithFirebaseAuthentication(APIView):
    """Base application 加上 firebase authentication"""
    renderer_classes = [JSONRenderer]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 在这里进行条件判断并设置属性
        # TODO:  settings.TEST need to change to DEBUG
        if not settings.TEST:
            self.authentication_classes = [FirebaseTokenAuthentication]
