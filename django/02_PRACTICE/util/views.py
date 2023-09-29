from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'util/index.html')

def clock(request):
    from datetime import datetime
    now_time = datetime.now()
    
    return render(request, 'util/clock.html', context = {
        'now_time' : now_time,
    })
    
    
def lotto_in(request):
    
    return render(request, 'util/lotto_in.html')

def lotto_out(request):
    # input
    import requests
    number1 = int(request.GET['number1'])
    number2 = int(request.GET['number2'])
    number3 = int(request.GET['number3'])
    number4 = int(request.GET['number4'])
    number5 = int(request.GET['number5'])
    number6 = int(request.GET['number6'])
    
    my = [number1, number2, number3, number4, number5, number6]
    
    # real lotto number and bonus / request from url
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
    data = res.json()
    
    real = [int(data[f'drwtNo{i}']) for i in range(1, 7)]
    bonus = data["bnusNo"]
    
    # nth prize determination
    same_count = 0
    for num in my:
        if num in real:
            same_count += 1
        
    prize = ''
    
    if same_count == 6:
        prize = '1'
    elif same_count == 5 and bonus in my:
        prize = '2'
    elif same_count == 5:
        prize = '3'
    elif same_count == 4:
        prize = '4'
    elif same_count == 3:
        prize = '5'
    
    result = f'{prize}등입니다. 축하합니다.'
        
    return render(request, 'util/lotto_out.html', context={
        'my': my,
        'real': real,
        'bonus': bonus,
        'result': result,
    })