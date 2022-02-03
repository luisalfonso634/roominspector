
from unicodedata import name
from django.urls import path
from users.views import ProfileList

urlpatterns = [
    path('api/', ProfileList.as_view(), name='profile_list'),
    path('api/<int:id>', ProfileList.as_view(), name='user_name'),
]



