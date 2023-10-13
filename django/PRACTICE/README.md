# Django 내장 회원 관리

1. app accounts django 의 내장 회원 관리 시스템의 존재 (urls.py& views.py)
2. signup, login, logout
    1. django.contrib.auth.forms 에 회원가입/로그인 Form 이미 존재
    2. django.contrib.auth 에 로그인/로그아웃 함수 이미 존재
3. python manage.py makemigrations , python manage.py migrate 로 한번에 진행
4. request.user.is_authenticated 를 통한 사용자 인증여부 확인


# User Article Comment
## login 여부에 따른 기능 접근성

Practice
1. Model Reply
    1. user  : user 정보
    2. student : student 정보
    3. content : 내용(CharField)
    4. rank : 평점(IntegerField)
2. User: Student = 1 : N
3. User : Reply = 1: N
4. Student : Reply = 1: N
5. 학생 디테일 페이지에서 Reply 작성
6. 로그인 하지 않으면 Student CUD 불가능, Reply CD 불가능
7. Reply 의 CRD
8. /univ/1/create
9.  /univ/1/delete
10. 조회는 학생 디테일 페이지에서 진행