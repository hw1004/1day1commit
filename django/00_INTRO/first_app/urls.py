# first_app/urls.py
from django.urls import path
from . import views # 지금 현재 위치에 있는 views.py

urlpatterns = [
    # first_app/hello/
    path('hello/', views.hello),
    # first_app/bye/
    path('bye/', views.bye),
    # URL pattern 'lotto/' => 화면에 로또번호 6개를 뽑아서 줌
    # first_app/lotto/
    path('lotto/', views.lotto),
    # first_app/lunch/
    path('lunch/', views.lunch),
]