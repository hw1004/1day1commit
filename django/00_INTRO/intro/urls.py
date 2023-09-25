"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
    

from django.contrib import admin
from django.urls import path, include

# first_app의 views.py에서 불러오기
# from first_app import views
# from second_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL hello/로 요청이 들어온면 ~~~(함수) 한다.
    # first_app의 views는 first_app 내의 urls.py로 분권화 시킨다.
    # first_app, second_app의 view가 하나의 urlpatterns에 들어가면
    # 중앙집권화되어 있어 어느 view를 참조하는 것인지 알기 어렵다.
    # x/hello/ 요청해야 원하는 페이지가 나옴
    path('first_app/', include('first_app.urls')),
    
    # second_app의 모든 패턴은 'second_app/'으로 시작
    # second_app/fibo/ 로 접속시 => view의 fibo 함수 실행
    # fibo는 피보나치 수열 10개를 fibo.html에서 사용자에게 보여줌 (ul > li)
    path('second_app/', include('second_app.urls'))
    
    # second_app/is_xmas/ 로 접속시 => view의 is_xmas 함수 실행
    # is_xmas 함수는 오늘이 크리스마스라면 YES를 
    # 아니라면 NO를 is_xmas.html에서 보여줌 (datetime 모듈 검색해서)
    
]



# http://127.0.0.1:8000/hello/
# 8000까지는 고정값
# req: /hello/
# res: 'Hello Django'