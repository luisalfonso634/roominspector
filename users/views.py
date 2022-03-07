"""Users views."""


import email
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import USERNAME_FIELD
from .serializers import UserSerializer
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email='email', password='password')
        print(user)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                status=status.HTTP_200_OK)
        else:
        # Si no es correcto devolvemos un error en la petición
            return Response(
                status=status.HTTP_404_NOT_FOUND)
    
    def __str__(self):
            """Return project title and first_name and last_name."""
            return f'{self.user.email} {self.user.password}'

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data 
        #if request.method == 'POST':
        email = data.get('email', None)
        print(email)
        password = data.get('password',None)
        print(password)
#AQUI ESTA EL PROBLEMA:
        user = authenticate(email=email, password=password) 
        print(user) 
        print("punto5")
        if user is not None: 
            if user.is_active:
                print("hola Miguel")
                login(request, user)
                print("punto6")
                return Response(status=status.HTTP_200_OK)
                print("punto7")
            else:
                print("punto8")
                return Response(
                status=status.HTTP_404_NOT_FOUND)
        else:
                print("punto9")
#                return Response(
#                status=status.HTTP_404_NOT_FOUND)



class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
