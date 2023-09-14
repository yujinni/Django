from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    prices = {
        "라면": 980,
        "홈런볼": 1500,
        "칙촉": 2300, 
        "식빵": 1800
    }
    thing_list = prices.keys()

    if thing in thing_list:
        price = prices.get(thing)
        total_price = price * int(cnt)
        message = f"{thing} {cnt}개의 가격은 {total_price}원입니다."
    else:
        total_price = 0
        message = f"{thing}은/는 없어용" 
    
    context ={
        'thing': thing,
        'cnt': cnt,
        'total_price': total_price,
        'message' : message,
        'thing_list': thing_list
    }

    return render(request, 'prices/price.html', context)