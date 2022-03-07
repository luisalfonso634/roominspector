#API

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from users.models import CustomUser
from django.db import models



class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name','password','username')

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
   

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name','password','username')

def validate_password(self, value):
    return make_password(value)