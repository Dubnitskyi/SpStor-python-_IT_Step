from django.urls import path

from . import views

app_name = 'myProject'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
