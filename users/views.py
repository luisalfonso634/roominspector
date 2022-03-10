"""Users views."""


from django.shortcuts import get_object_or_404
from rest_framework import status, generics

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

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, BaseBackend


class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny] 
    
    def post(self, requests):
        content = {
                   'user': str(requests.user),  # `django.contrib.auth.User` instance.
                   'auth': str(requests.auth),  # None
                }
        return Response(content)    
  
    def login_view(self,request):
        if request.method == 'POST':
            #USERNAME_FIELD = request.data.get('email', None)
            USERNAME_FIELD= request.POST['email']
            print(USERNAME_FIELD)
            password = request.POST[password]
            print(password)
            #password = request.data.get('password',None)
            #AQUI ESTA EL PROBLEMA:
            user = authenticate(request, password=password, username=USERNAME_FIELD)
            print('hola'+" "+ str(user))
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
