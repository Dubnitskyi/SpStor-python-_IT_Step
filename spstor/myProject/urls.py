from django.urls import path

from . import views

app_name = 'myProject'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('library/', views.library, name='library'),
    path('games/', views.games, name='games'),
    path('categories', views.categories, name='categories'),
]
