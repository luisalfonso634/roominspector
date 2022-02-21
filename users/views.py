"""Users views."""

from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
<<<<<<< HEAD
from django.utils.datastructures import MultiValueDictKeyError


class LoginView(APIView):
    
    def post(self, request):
        if request.method == 'POST':
            print("punto1")
            email = request.POST.get('email', False)
            print(email)
            password = request.POST.get('password',False)
            print("punto3")
            user = authenticate(request, email=email, password=password)
            print("punto4")
            print(user)
            print("punto5")
            if user: #AQUI ESTA EL PROBLEMA
                #print("hola Miguel")
                login(request, user)
                print("punto6")
                return Response(UserSerializer(user).data,
                status=status.HTTP_200_OK)
                print("punto7")
            else:
                print("punto8")
                return Response(
                status=status.HTTP_404_NOT_FOUND)
=======


class LoginView(APIView):
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)
>>>>>>> 14d8ea251be4795ec19939cd38599e75b7c1f05c


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

<<<<<<< HEAD
class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

=======
>>>>>>> 14d8ea251be4795ec19939cd38599e75b7c1f05c
        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
