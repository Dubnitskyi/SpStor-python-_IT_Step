from django.shortcuts import render

def index(request):
    return render(request, 'myProject/index.html')

def about(request):
    return render(request, 'myProject/about.html')

def login(request):
    return render(request, 'myProject/login.html')

def register(request):
    return render(request, 'myProject/register.html')

def library(request):
    return render(request, 'myProject/library.html')

def games(request):
    return render(request, 'myProject/games.html')

def categories(request):
    return render(request, 'myProject/categories.html')