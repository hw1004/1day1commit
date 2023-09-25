# Django

> **Django**는 웹사이트를 쉽고 빠르게 개발할 수 있도록 도움을 주는 *웹 프레임워크*이다. 프랜차이즈 시스템 아래에서 더 쉽게 카페 창업을 할 수 있는 것을 생각하면 쉽게 이해할 수 있다. Django는 분류된 파일들에 대해 일련의 단계를 수행하는 코드로 구성되어 있다.

![django](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction/basic-django.png)

## MVT(Model View Template)
|elements|description|
|---|---|
|URLs|분리된 뷰 함수를 작성하여 각각의 리소스 유지보수를 용이하게 함|
|View|HTTP 요청을 수신하고 응답을 반환하는 요청 처리 함수|
|Models|응용프로그램의 데이터 구조를 정의하고 db의 기록을 관리하고 쿼리하는 방법을 제공하는 파이썬 객체|
|Templates|파일의 구조 및 레이아웃 정의, 실제 내용을 보여주는 데 사용되는 텍스트 파일|

## Django project
```
# 1. install Django 및 시작
# project를 시작할 폴더에 장고 설치
pip install django

# project file 생성
django-admin startproject 00_Intro

# 2. app 생성
python manage.py startapp first_app

# app을 생성했으면 먼저 intro 폴더의 
# settings.py > installed_app 부분에 first_app을 입력한다.(출생신고)
```

3. views.py
- `HttpResponse 또는 render`을 사용해서 function view를 만든다. (함수 생성)

4. tempaltes 생성과 html 파일 생성
- views.py 안의 함수들은 개개인의 html 파일을 templates이라는 폴더를 만들어 생성해야 한다.
- html 파일 내에는 실제로 웹에서 어떻게 보일지를 조정한다.
- `render(request, 'lotto.html', context)`에서 context를 마지막에 붙였다. return 이전에 context를 dictioanry로 지정해주면 지정된 값은 lotto.html 파일에서 사용될 수 있다. 따라서 코드로 계산된 값들이나 텍스트 등을 html로 끌고 와서 사용할 수 있게 된다.

5. urls.py
|urls.py|description|
|---|---|
|intro의 urls.py|`include`를 이용해 first_app과 추후의 다른 second_app에 포함되는 function view를 분권화함. first와 second의 views를 명확히 구분시키기 위함.|
|first_app의 urls.py|자동으로 생성되지 않기 때문에 따로 만들어준다. first_app에 포함되는 함수들을 urlpattern에 넣는다.|

- 따라서 intro의 urls.py는 `path('first_app', include(first_app.urls))`로
- first_app의 urls.py 파일에 있는 views를 불러온다.
- first_app의 urls.py 파일에서 views는 views.py로부터 불러온다.

5. runserver
`python manage.py runserver`을 실행하고 고정값 http://127.0.0.1:8000/ 뒤에 customizing 해주면 원하는 function view의 html 파일을 웹으로 확인할 수 있다.
- (Ex) http://127.0.0.1:8000/first_app/lotto/