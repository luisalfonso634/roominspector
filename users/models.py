#User
#16FEB22
from django.contrib.auth.models import AbstractUser
from django.db import models

from roominspectorapi.settings import AUTH_USER_MODEL



class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
      
class Meta:
        model = AUTH_USER_MODEL
        fields = ('id', 'email', 'first_name', 'last_name','password','username')


USERNAME_FIELD = 'email'  # new


REQUIRED_FIELDS = ['username', 'password']  # new










