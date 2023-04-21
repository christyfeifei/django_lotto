from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def today(request):
    from datetime import datetime
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date)  # 印出字串在console端
    return HttpResponse(date)  # 封裝後、回傳在前端
