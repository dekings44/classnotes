from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLogin


app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.account_register, name = 'register'),
    path('profile/', views.profile, name ='profile'),
   
]