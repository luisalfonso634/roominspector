
from django.urls import path, include
from .views import LoginView, LogoutView, SignupView

urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),

    path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

    path('auth/signup/',
         SignupView.as_view(), name='auth_signup'),

    
    ]



