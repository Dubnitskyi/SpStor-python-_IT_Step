from django.shortcuts import render
from .models import Categorie,Game

def index(request):
    return render(request, 'myProject/index.html')

def about(request):
    return render(request, 'myProject/about.html')
def library(request):
    return render(request, 'myProject/library.html')

def games(request):
    games = Game.objects.all()
    context = {'games':games}
    return render(request, 'myProject/games.html',context = context)

def categories(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'myProject/categories.html',context = context)

def categori_game(request , categori_id):
    categori = Categorie.objects.get(id=categori_id)
    games = Game.objects.all()
    context = {'games': games,
               'categori': categori}
    return render(request, 'myProject/categori_game.html',context = context)