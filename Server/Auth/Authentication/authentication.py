
import os
from rest_framework.permissions import BasePermission
import firebase_admin
# from firebase_admin import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
# cred = credentials.Certificate('path_to_your_serviceAccountKey.json')
# firebase_admin.initialize_app(cred)

#  ----------------------------------------------------------------

current_script_directory = os.path.dirname(os.path.abspath(__file__))

# 获取项目的根目录（假设您的脚本文件位于项目根目录下的某个子目录中）
project_root_directory = os.path.dirname(current_script_directory)

# 使用项目的根目录构建配置文件的路径
config_file_path = os.path.join(
    project_root_directory, "./Backend/firebaseconfig.json")
# firebase
cred = credentials.Certificate(
    "./Backend/firebaseconfig.json")
firebase_admin.initialize_app(cred)


class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        header = request.headers.get("Authorization")

        if header and header.startswith("Bearer "):
            token = header.replace("Bearer ", "")
            try:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token["uid"]
                email = decoded_token["email"]

                # 返回驗證成功的用戶
                return (uid, None)
            except Exception as e:
                raise AuthenticationFailed(str(e))

        return None


class FirebaseTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # 从请求头中获取 Firebase Tokens
        header = request.headers.get("Authorization")

        if header and header.startswith("Bearer "):
            token = header.replace("Bearer ", "")
            try:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token["uid"]
                email = decoded_token["email"]
                
                # TODO: test auth
                request.uid = uid
                
            
                # 返回驗證成功的用戶
                return (uid, None)
            except Exception as e:
                raise AuthenticationFailed(str(e))
        else:
            raise AuthenticationFailed("Header has no authorization token")


# permissions.py


class HasLevelFivePermission(BasePermission):
    def has_permission(self, request, view):
        return True


class HasLevelOnePermission(BasePermission):
    def has_permission(self, request, view):
        # print(request.user)
        if not request.user.is_authenticated:
            return False

        return request.user.level >= 1


class HasLevelThreePermission(BasePermission):
    def has_permission(self, request, view):
        # 檢查使用者是否已通過身份驗證
        if not request.user.is_authenticated:
            return False

        # check permissions
        return request.user.level >= 3
