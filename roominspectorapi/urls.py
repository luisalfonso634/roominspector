"""roominspectorapi URL Configuration"""
# Django
from django.urls import path, include
#API
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('users.urls'), name='users'),
]   

