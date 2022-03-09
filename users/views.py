"""Users views."""


from contextvars import Token
import email
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import USERNAME_FIELD
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse


from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
#7mar22
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend




class LoginView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [AllowAny] 
    
    def post(self, requests):
        # content = {
        #            'user': str(requests.user),  # `django.contrib.auth.User` instance.
        #            'auth': str(requests.auth),  # None
        #         }
        # return Response(content)    
        # def authenticate(self):
        #     return authenticate(
        #     USERNAME_FIELD=self.user.USERNAME_FIELD,
        #     password=self.cleaned_data['password'])

        if requests.method == 'POST':
            USERNAME_FIELD = requests.data.get('email', None)
            print(USERNAME_FIELD)
            password = requests.data.get('password',None)
            print(password)
            #AQUI ESTA EL PROBLEMA:
            user = authenticate(password=password, email=USERNAME_FIELD)
            print('hola'+" "+ str(user))
        if  user : 
            login(requests, user)
            print("punto1")
            return Response(status=status.HTTP_200_OK)
    
        return Response(
            status=status.HTTP_404_NOT_FOUND)



class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
