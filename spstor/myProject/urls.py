from django.urls import path

from . import views

app_name = 'myProject'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('library/', views.library, name='library'),
    path('games/', views.games, name='games'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:categori_id>', views.categori_game, name='categori_game'),
    path('games/<int:game_id>', views.game_info, name='game_info'),
    path('new_categori/', views.new_categori, name='new_categori'),
    path('new_game/', views.new_game, name='new_game'),
]
