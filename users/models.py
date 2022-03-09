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
<<<<<<< HEAD
    email = models.EmailField(max_length=150, unique=True)
    employee_category=models.CharField(max_length=10, choices=categories)
=======
        
        email = models.EmailField(
        max_length=150, unique=True)

#class CategoryUser(models.Model):    
#    model = CustomUser
#    manager = models.ManyToManyField('self')
#    supervisor = models.ManyToManyField('self')
#    hk_employee = models.ManyToManyField('self')
>>>>>>> 497858990e606d4b301915f75c6f2106a9def982

    
    
class Meta:
    model= AUTH_USER_MODEL
    fields = ('id', 'first_name', 'last_name','password','username','employee_category')


USERNAME_FIELD = 'email'  # new


REQUIRED_FIELDS = ['username', 'password','employee_category']  # new








