from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import ExpansionForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    expansion_form = ExpansionForm()
    return render(request, 'games/detail.html', {'game': game, 'expansion_form': expansion_form})

def add_expansion(request, game_id):
    form = ExpansionForm(request.POST)
    if form.is_valid():
        new_expansion = form.save(commit=False)
        new_expansion.game_id = game_id
        new_expansion.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['platform', 'description', 'relyear']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'
