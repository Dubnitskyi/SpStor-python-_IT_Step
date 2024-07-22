from django.shortcuts import render, redirect

from .forms import CategoryForm,GameForm
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

def game_info(request , game_id):
    game = Game.objects.get(id=game_id)
    games = Game.objects.all()
    context = {'game': game,'games':games}
    return render(request, 'myProject/game_info.html',context = context)


def new_categori(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myProject:categories')
    context = {'form': form}
    return render(request, 'myProject/new_categori.html',context = context)

def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myProject:games')
    context = {'form': form}
    return render(request, 'myProject/new_game.html', context=context)