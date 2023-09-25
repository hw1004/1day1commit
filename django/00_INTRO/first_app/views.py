from django.shortcuts import render
from django.http import HttpResponse

# 1. function view*
# 2. class view


# Create your views here.
# function view
def hello(request):
    return HttpResponse('Hello Django')

def bye(request):
    # bye.html 을 랜더하도록 하자.
    # 파일 안에는 적당히 h1, p 내용 쓰기
    return render(request, 'bye.html')

def lotto(request):
    import random
    lotto_num = []
    for i in range(6):
        lotto_num.append(random.randint(1,46))
    lotto_num.sort()
        
    context = {
        'message' : '부자되고싶다',
        'lotto_num': lotto_num,
    }
    
    # return HttpResponse(lucky)
    return render(request, 'lotto.html', context)

# /lunch/ => lunch view function => 여러 메뉴들 중에 하나 뽑아서
# => 시용자에게 HTML로 보여줌

def lunch(request):
    import random
    menus = ['apple', 'tteokboki', 'sushi', 'chicken']
    choice = random.choice(menus)
    
    context = {
        'choice' : choice,
    }
    
    return render(request, 'lunch.html', context)

    # context으로 안 쓰고 dictionary를 바로 넣기도 함
    # return render(request, 'lunch.html', {
    #     'menu': menu,
    # })
        