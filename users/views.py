"""Users views."""


from contextvars import Token
import email
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
import users

from users.models import USERNAME_FIELD
from .serializers import UserSerializer
from django.utils.datastructures import MultiValueDictKeyError
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
from django.contrib.auth.backends import ModelBackend

class CustomEmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny] 
    
    def post(self, request):
        content = {
                    'user': str(request.user),  # `django.contrib.auth.User` instance.
                    'auth': str(request.auth),  # None
                }
        return Response(content)        
        if request.method == 'POST':
            email = request.data.get('email', None)
            print(email)
            password = request.data.get('password',None)
            print(password)
            #AQUI ESTA EL PROBLEMA:
            user = authenticate(request, USERNAME_FIELD= "username", password= "pasword")
            print(user)
        if  user : 
            login(request, user)
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
