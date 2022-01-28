"""roominspectorapi URL Configuration"""
# Django
from django.urls import path, include
#API
from django.conf import settings
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [

    path(r'admin/', admin.site.urls, name='admin'),
    path(r'api/v1/', include('users.urls'), name='api'),
]   
urlpatterns += [
    path(r'api/v1/auth', include('rest_framework.urls', namespace='rest_framework' ))
]
