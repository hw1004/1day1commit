from django.shortcuts import render

# Create your views here.
def hello(request, name):
    print(name)   # keyword argument
    message = f'반갑습니다. {name}'
    return render(request, 'user_input/hello.html', {
        'message': message,
    })
    
def ping(request):
    
    return render(request, 'user_input/ping.html')

def pong(request):
    username = request.GET['username']     # ping으로부터 요청이 왔을 때 시행
    password = request.GET['password']
    return render(request, 'user_input/pong.html', {
        'username': username,
        'password': password,
    })