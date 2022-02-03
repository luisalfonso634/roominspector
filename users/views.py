"""Users views."""

#API
import profile
from django.http import JsonResponse
#from rest_framework import generics
#from users.serializers import ProfileSerializer
#from django.shortcuts import get_object_or_404
from users.models import Profile
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


#API
class ProfileList(View):
    #con esta instruccion estoy listando todos los usuarios a traves del ORM
    #El Serializer lo quite para probar otro metodo
    #serializer_class = ProfileSerializer
    #el dispatch lo estoy haciendo para decirle que no haga la verificacion csrf
    #dispatch es un metodo que se ejecuta cada vez que hacemos una peticion


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):
        if (id>0):
            queryset=list(Profile.objects.filter(id=id).values())
            if len(queryset)>0:
                profile = queryset[0]
                datos = {'message':"Success", 'users':profile}
            else:
                datos = {'message':"User not found"}
            return JsonResponse(datos)
        else:
            queryset = list(Profile.objects.values())
            if len(queryset) > 0:
                datos = {'message':"Success", 'users':queryset}
            else:
                datos = {'message':"Users not found"}
            return JsonResponse(datos)


    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        Profile.objects.create(first_name=jd['first_name'], 
                             last_name = jd['last_name'], 
                                  email = jd['email'])

        #print(jd)
        datos = {"message":"Success"}
        return JsonResponse(datos)

        
        #request, esta establecido como parametro en cada una de las funciones
        #body, es el cuerpo de la peticion
    
        



    def put(self, request, id):
        jd = json.loads(request.body)
        profile=list(Profile.objects.filter(id=id).values())
        if len(profile) > 0:
            profile = Profile.objects.get(id=id)
            profile.first_name = jd['first_name'] 
            profile.last_name = jd['last_name'] 
            profile.email = jd['email'] 
            profile.save()  
            datos = {'message':"Update User"}       
        else:
            datos = {'message':"User not found"}
        return JsonResponse(datos)


    def delete(self, request, id):
        profile=list(Profile.objects.filter(id=id).values())
        if len(profile) > 0:
            Profile.objects.filter(id=id).delete()
            datos = {'message':"User Deleted"} 
        else:
            datos = {'message':"User not found"}
        return JsonResponse(datos)






        
    

