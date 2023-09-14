from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {}
    return render(request, 'my_app/hello.html', context)