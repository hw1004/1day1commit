from django.shortcuts import render, redirect
# redirect는 강제적으로 특정 페이지로 넘어가게 하는 것

from .models import Article
from .forms import ArticleForm

# Create
# def new(request):
    # form = ArticleForm()   # input tag 대신 생성
    # return render(request, 'board/new.html', {
        # 'form': form,
    # })   # 비어있음

def create(request):   # 저장하는 과정
    if request.method == 'GET':
        form = ArticleForm()   # input tag 대신 생성
        
    # 데이터 입력
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
    
        # 데이터 검증
        # is가 붙으면 bool (T,F)
        if form.is_valid():   # validation (유효성 검증)
            # 저장
            article = form.save()
            # f'/board/{article.pk}/'
            return redirect('board:detail', article.pk)
    
    return render(request, 'board/form.html', {
        'form': form,
    })   # 채워져 있는 form을 검증 후 그 결과물임
    
    # article = Article()
    # 채우기
    # title = request.POST['title']
    # content = request.POST['content']  
    
    # article.title = title
    # article.content = content
    # 저장
    # article.save()
    

    
# Read
def index(request):
    # 모든 게시글 조회
    articles = Article.objects.all()
        
    return render(request, 'board/index.html', {
        'articles': articles,
    })

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })

# Update
# def edit(request,pk):
    # article = Article.objects.get(pk=pk)
    # instance는 수정할 때 기존 글 가져옴
    # form = ArticleForm(instance=article)
    # return render(request, 'board/edit.html', {
        # 'article': article,
        # 'form': form,
    # })

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'GET':
        form = ArticleForm(instance=article)
    # 데이터 입력
    
    
    # 데이터 검증
    # is가 붙으면 bool (T,F)
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():   # validation (유효성 검증)
            # 저장
            article = form.save()
            # f'/board/{article.pk}/'
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form': form,
    })    # 채워져 있는 form을 검증 후 그 결과물임
        
    #article = Article.objects.get(pk=pk)
    #title = request.POST['title']
    #content = request.POST['content']
    #article.title = title
    #article.content = content
    #article.save()
    # f'/board/{article.pk}/'
    #return redirect('board:detail', article.pk)

# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')


# /board/new/ => new 함수 실행 => new.html return (사용자 글을 쓸 곳 - 내용 비워두기)
# /board/create/ => create 함수 실행 => 내용 비워놓기
# /board/ => index 함수 실행 => index.html return (글 목록)
# /board/<int:pk>/ => detail 함수 실행(pk는 변수 라우팅) => detail.html return (글 상세보기)
# /board/edit/ => edit 함수 실행 => edit.html return(글 수정할 곳)
# /board/update/ => update 함수 실행 => 내용 비워두기
# /board/delete/ => delete 함수 실행 => 내용 비워두기