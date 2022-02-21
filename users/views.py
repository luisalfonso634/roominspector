"""Users views."""


from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.utils.datastructures import MultiValueDictKeyError


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data 
        #if request.method == 'POST':
        email = data.get('email', None)
        password = data.get('password',None)
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
