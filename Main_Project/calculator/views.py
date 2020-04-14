from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'calculator/home.html')


def addition(request):
    num1=int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1+num2
    return render(request,'calculator/addition.html',{'result':res})

def subtraction(request):
    num1=int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1-num2
    return render(request,'calculator/subtraction.html',{'result':res})

def multiplication(request):
    num1=int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1*num2
    return render(request,'calculator/multiplication.html',{'result':res})

def division(request):
    num1=int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    res = num1/num2
    return render(request,'calculator/division.html',{'result':res})