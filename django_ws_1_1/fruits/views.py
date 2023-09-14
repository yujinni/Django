from django.shortcuts import render

# Create your views here.
def fruit(request):
    fruit_name = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과", "구아바"]

    context = {
        'fruit' : fruit_name,
        'hate' : hate
    }

    # 어떤 화면을 보여줄지 return
    return render(request, 'fruits/fruit.html', context)