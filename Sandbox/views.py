import json
from django.shortcuts import render

# api
from drfa.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status

# _mock
from Sandbox.mock.restaurant import get_mock_r, get_mock_menu
from Sandbox.mock.user import get_user_mack


#  ----------------------------------------------------------------


@api_view(['GET'])
def get_shop(request, id=None):

    if id is None:
        with open('Sandbox/mock/all_shop.json', 'r') as file:
            data = json.load(file)
        return Response(data, status=status.HTTP_200_OK)
    else:
        with open('Sandbox/mock/shop.json', 'r') as file:
            data = json.load(file)
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def ger_shop_current(request):
    with open('Sandbox/mock/current.json', 'r') as file:
        data = json.load(file)
    return Response(data, status=status.HTTP_200_OK)


class Auth(APIView):
    def get(self, request, uid=None):
        return Response(get_user_mack())

    def post(self, request, uid=None):
        return Response(get_user_mack(), status=status.HTTP_201_CREATED)

    def put(self, request, uid=None):
        return Response(status=status.HTTP_201_CREATED)
