#User
from django.contrib import admin


#from roominspectorapi.settings import AUTH_USER_MODEL
#7mar22
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone


from roominspectorapi.settings import AUTH_USER_MODEL
from .choices import categories



class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    employee_category=models.CharField(max_length=10, choices=categories)

    
    
class Meta:
    model= AUTH_USER_MODEL
    fields = ('id', 'first_name', 'last_name','password','username','employee_category')


USERNAME_FIELD = 'email'  # new


REQUIRED_FIELDS = ['username', 'password','employee_category']  # new








