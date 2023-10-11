from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # 상수(값이 초기화/할당 이후 절대 변하면 안된다는 뜻)
    CHOICES = [
        ('SOC', '사회학'),
        ('POL', '정치외교학'),
        ('PSY', '심리학'),
        ('CSE', '컴퓨터공학')
    ]
    
    name = forms.CharField(min_length=1, max_length=10)
    age = forms.IntegerField(min_value=10, max_value=200)
    major = forms.ChoiceField(
        widget=forms.Select(),
        choices=CHOICES
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        min_length=5
    )
    
    class Meta:
        model = Student
        fields = '__all__'



# PRACTICE > crud app 에서 ModelForm 사용하기
 # crud/forms.py 생성
# forms.py 에 StudentForm 이라는 모델폼 생성
# 모델은 Student
# 필드는 모든 필드
# new.html 과 edit.html 에서 <form> 의 제출 방식(method) 를 모두 POST 로 교체
# 토큰 잊지 않기
# new.html 과 edit.html 에서 <input> 요소들 모두 form 에서 출력하도록 교체
# create 와 update 에서 사용자 입력을 검증
# 유효할 경우에만 저장.
# 유효하지 않을 경우, 에러메세지와 함꼐 html 다시 렌더