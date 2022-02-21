#User
#16FEB22
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True)
      
<<<<<<< HEAD
#class Meta:
#        model = CustomUser
#        fields = ('username', 'email', 'password')
=======
    
>>>>>>> 14d8ea251be4795ec19939cd38599e75b7c1f05c


USERNAME_FIELD = 'email'  # new


REQUIRED_FIELDS = ['username', 'password']  # new










