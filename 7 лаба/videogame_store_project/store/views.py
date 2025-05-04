# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Igra
from django.contrib.auth.decorators import login_required

def index(request):
    games = Igra.objects.all()
    context = {
        'games': games
    }
    return render(request, 'store/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def game_detail(request, pk):
    game = get_object_or_404(Igra, pk=pk)
    context = {
        'game': game
    }
    return render(request, 'store/game_detail.html', context)

@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'store/profile.html', context)