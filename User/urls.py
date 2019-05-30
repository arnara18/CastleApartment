from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', LoginView.as_view(template_name='User/SignIn.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]
