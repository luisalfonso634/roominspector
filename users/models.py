#User
#16FEB22

from django.contrib.auth.models import AbstractUser
from django.db import models

#from roominspectorapi.settings import AUTH_USER_MODEL
#7mar22
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from roominspectorapi.settings import AUTH_USER_MODEL

class CustomUser(AbstractUser):
        
        email = models.EmailField(
        max_length=150, unique=True)

#class CategoryUser(models.Model):    
#    model = CustomUser
#    manager = models.ManyToManyField('self')
#    supervisor = models.ManyToManyField('self')
#    hk_employee = models.ManyToManyField('self')

class Meta:
        model= AUTH_USER_MODEL
        fields = ('id', 'first_name', 'last_name','password','username')


USERNAME_FIELD = 'email'  # new


REQUIRED_FIELDS = ['username', 'password']  # new








