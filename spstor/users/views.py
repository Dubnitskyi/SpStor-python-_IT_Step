from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            redirect('myProject:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)