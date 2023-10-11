from django.contrib import admin
from django.urls import path
from . import views

# URL을 변수로 사용 (app_name:name)
app_name = 'crud'

urlpatterns = [
    # path('new/', views.new, name='new'),   # crud:new
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

