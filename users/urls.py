
from django.urls import path, include
from .views import LoginView, LogoutView, SignupView

urlpatterns = [
    # Auth views
<<<<<<< HEAD
    path('auth/login/',
         LoginView.as_view(), name='login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

    path('auth/signup/',
=======
     path('auth/login/',
         LoginView.as_view(), name='auth_login'),

     path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

     path('auth/signup/',
>>>>>>> 14d8ea251be4795ec19939cd38599e75b7c1f05c
         SignupView.as_view(), name='auth_signup'),

    
    ]



