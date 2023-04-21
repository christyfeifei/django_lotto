from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.


def index(request):
    return render(request, 'index.html')


def today(request):
    from datetime import datetime
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(date)  # 印出字串在console端
    return HttpResponse(date)  # 封裝後、回傳在前端


"""
1. 產生樂透號碼
2. 號碼不重覆(排序)+特別號
3. 4,13,15,21,38,44 特別號:42
"""


def get_lotto(count=6):
    lottos = []
    while True:
        x = random.randint(1, 49)
        if x not in lottos:
            lottos.append(x)

        if len(lottos) == count:
            break

    lottos.sort()
    lottos.append(random.randint(1, 49))
    # 把lottos六個號碼轉字串(str)後、用","隔開，並去掉特別號[:-1]
    result = ','.join(map(str, lottos[:-1]))+f' 特別號:{lottos[-1]}'

    return result


print(get_lotto())
