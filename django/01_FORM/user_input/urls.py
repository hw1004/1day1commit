from django.urls import path
from . import views

urlpatterns = [
    # 변수인데 name이라는 변수명으로 받고 str 처리
    path('hello/<str:name>/', views.hello),
    path('ping/', views.ping),
    path('pong/', views.pong),
]
