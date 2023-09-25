# first_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('fibo/', views.fibo),
    
    path('is_xmas/', views.is_xmas),
]
