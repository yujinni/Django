import random
from django.shortcuts import render



# Create your views here.
def certification1(request):
    age = range(25,31)
    picked_age = random.choice(age)

    grade = ['a','b','c','s']
    picked_grade = random.choice(grade)

    context = {
        'age': picked_age,
        'grade': picked_grade
    }
    return render(request, 'certifications/certification1.html', context)

def certification2(request):
    age = range(25,31)
    picked_age = random.choice(age)

    grade = ['a','b','c','s']
    picked_grade = random.choice(grade)

    context = {
        'age': picked_age,
        'grade': picked_grade
    }
    return render(request, 'certifications/certification2.html', context)

def certification3(request):
    age = range(25,31)
    picked_age = random.choice(age)

    grade = ['a','b','c','s']
    picked_grade = random.choice(grade)

    context = {
        'age': picked_age,
        'grade': picked_grade
    }
    return render(request, 'certifications/certification3.html', context)