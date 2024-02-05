from helper.base.base_import_view import *
from django.middleware import csrf

@method_decorator(base_protection_decorators_v0 , name="dispatch")
class GetTokenAPIView(BaseAPIViewWithFirebaseAuthentication):
    def get(self, request):
        token = csrf.get_token(request)
        return Response({'token': token})
