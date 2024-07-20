from django.shortcuts import render
from .models import Categorie,Game

def index(request):
    return render(request, 'myProject/index.html')

def about(request):
    return render(request, 'myProject/about.html')
def library(request):
    return render(request, 'myProject/library.html')

def games(request):
    return render(request, 'myProject/games.html')

def categories(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'myProject/categories.html',context = context)