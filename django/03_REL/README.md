# Django 내장 회원 관리

1. get_object_or_404
2. 함수마다 요청 메서드 데코레이터 붙이기 (require_safe, require_POST, require_http_methods)
3. delete 요청도 DB에 변화를 주기때문에 POST 로 바꾸기
4. Admin 페이지와 python manage.py createsuperuser
5. django 의 내장 회원 관리 시스템의 존재
    a. 사용자 커스터마이즈 하지 않으면 Model과 Form 정의 불필요
    b. django.contrib.auth.forms 에 회원가입/로그인 Form 이미 존재
    c. django.contrib.auth 에 로그인/로그아웃 함수 이미 존재
6. python manage.py makemigrations , python manage.py migrate 로 한번에 진행
7. accounts 앱 => 회원관리 전반을 담당
8. 기존 코드와 굉장히 유사함
9. request.user 의 존재와 AnonymousUser
10. 회원가입/로그인의 실제 의미 (쿠키/세션)