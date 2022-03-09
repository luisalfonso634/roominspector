
from django.urls import path, include
from .views import LoginView, LogoutView, SignupView
from rest_framework.authtoken import views
from rest_framework.authtoken import views



urlpatterns = [
    # Auth views
     path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

     path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

     path('api-token-auth/', views.obtain_auth_token)
    
    ]



