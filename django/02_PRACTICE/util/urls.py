from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    
    path('clock/', views.clock),
    
    path('lotto_in/', views.lotto_in),
    
    path('lotto_out/', views.lotto_out),
]
