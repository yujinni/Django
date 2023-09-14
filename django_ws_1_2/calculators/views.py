from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request,'calculators/calculation.html')

def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    sub = int(num1) - int(num2)
    mul = int(num1) * int(num2)
    if num2 != '0':
        div = int(num1) / int(num2)
    else:
        div = '계산할 수 없습니다.'
    context = {
        'num1' : num1,
        'num2' : num2,
        'sub' : sub,
        'mul' : mul,
        'div' : div,
    }
    return render(request,'calculators/result.html',context)

