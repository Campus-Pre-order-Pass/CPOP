# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# rest_framework
from rest_framework import status

# MarkData
from Order.OrderLogic.test.mark import MarkData

# BaseAPIViewDRFConfig
from helper.base.drf_yasg_base import BaseAPIViewDRFConfig

# serializers
from Order.serializers import *
from MenuItem.serializers import *
from rest_framework.views import APIView


class DRF(APIView):
    """drf_yasg app configuration"""
    
    GetTokenAPIView = {
        "GET":{
             "operation_summary": "獲取 X_CSRF_TOKEN",
            "operation_description": "獲獲取 X_CSRF_TOKEN`",
            'manual_parameters': [
                BaseAPIViewDRFConfig.FIRE_BASE_HEADER,
            ],
            
        "responses": 
            {
                status.HTTP_200_OK : openapi.Response(
                    description="回傳token", 
                    examples={
                        "application/json": {
                            "token": "1234567890xrrctfvygbuhinjpmok"                            
                        }
                    }
                )
            }
        }
    }