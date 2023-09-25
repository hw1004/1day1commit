from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fibo(request):
    fibo_list = []
    for i in range(1,11):
        if i <= 2:
            fibo_list.append(i)
        elif i > 2:
            fibo_list.append(fibo_list[i-2] + fibo_list[i-3])
            
    context = {
        'message': '피보나치 수열',
        'fibo_list': fibo_list,
    }
    return render(request, 'fibo.html', context)

def is_xmas(request):
    from datetime import date
    
    today = date.today()
    month = today.month
    day = today.day
    isxmas = ""
    
    if month == '12' and day == '25':
        isxmas += "YES"
    else:
        isxmas += "NO"
        
    context = {
        'message': '오늘은 크리스마스입니까?',
        'isxmas' : isxmas,
    }
        
        
    return render(request, 'is_xmas.html', context)
        
