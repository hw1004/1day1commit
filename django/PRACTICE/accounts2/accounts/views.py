from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 요청 보낸 사용자가 로그인 상태라면 돌려보내기
    if request.user.is_authenticated:
        return redirect('board:index')
    
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('board:index')  # login 했으면 login 페이지에 접근 못하게
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # 쿠키(팔찌 세팅)
            auth_login(request, user)
            print(user)
            return redirect('board:index')
        
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {
        'form': form,
    })
    

def logout(request):
    if not request.user.is_authenticated:
        return redirect('board:index')
    
    auth_logout(request)
    return redirect('board:index')