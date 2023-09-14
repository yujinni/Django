from django.shortcuts import render


def first(request):
    message = None  # 초기 출력 화면에 아무것도 받지 못함을 나타내기 위해
    context = {
        'message': message,
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'throw_catch/second.html', context)
