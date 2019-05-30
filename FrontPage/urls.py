from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('properties', include('Properties.urls'))
]
