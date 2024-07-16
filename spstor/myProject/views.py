from django.shortcuts import render

def index(request):
    return render(request, 'myProject/index.html')

def about(request):
    return render(request, 'myProject/about.html')