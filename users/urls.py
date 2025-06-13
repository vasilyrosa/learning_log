"""Definir padrão de url para users"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    #página de login
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    
    #página de logout
    path('logout/', views.logout_view, name='logout'),
    
    #página de cadastro
    path('register/', views.register, name='register'),
]