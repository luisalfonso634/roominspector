"""Users views."""

from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
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



class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
