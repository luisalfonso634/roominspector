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

<<<<<<< HEAD


=======

class CustomEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
>>>>>>> 497858990e606d4b301915f75c6f2106a9def982

class LoginView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [AllowAny] 
    
<<<<<<< HEAD
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
=======
    def post(self, request):
        content = {
                    'user': str(request.user),  # `django.contrib.auth.User` instance.
                    'auth': str(request.auth),  # None
                }
        return Response(content)    

        #if request.method == 'POST':
        #    email = request.data.get('email', None)
        #    print(email)
        #    password = request.data.get('password',None)
        #    print(password)
        #    #AQUI ESTA EL PROBLEMA:
        #    user = authenticate(request, username= "username", password= "password")
        #    print(user)
        #if  user : 
        #    login(request, user)
        #    print("punto1")
        #    return Response(status=status.HTTP_200_OK)
>>>>>>> 497858990e606d4b301915f75c6f2106a9def982
    
        #return Response(
        #    status=status.HTTP_404_NOT_FOUND)



class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
