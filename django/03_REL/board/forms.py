from django import forms
from .models import Article, Comment
# 1. 입력 데이터 검증 과정 X
# 2. HTML 만들기 귀찮다

class ArticleForm(forms.ModelForm):
    
    # django 에서 문자열을 검증할 필드
    title = forms.CharField(min_length=2, max_length=20)
    content = forms.CharField(  
        min_length=5,
        max_length=500,
        # forms.CharField는 기본값이 input type text
        # widget을 통해 HTML 코드도 바꿀 수 있음
        widget=forms.Textarea(
            attrs={'class': 'my-class'}
        )
    )
   
    class Meta:
        model = Article
        # fields = ('title', 'content')
        exclude = ('user', )  # user만 빼고
        # fields = (title, )   # title에 대한 입력 화면만 나옴

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content', )
        # exclue = ('user','article', )