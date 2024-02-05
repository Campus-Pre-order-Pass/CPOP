from helper.base.base_import_view import *
from django.middleware import csrf


class GetTokenAPIView(BaseAPIViewWithFirebaseAuthentication):
    def get(self, request):
        token = csrf.get_token(request)
        return Response({'token': token})
