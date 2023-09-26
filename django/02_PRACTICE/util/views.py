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