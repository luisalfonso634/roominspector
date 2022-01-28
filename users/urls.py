
from unicodedata import name
from django.urls import path
from users.views import ProfileList

urlpatterns = [
    path('users/', ProfileList.as_view(), name='users')

]



