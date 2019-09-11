from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Player
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
    players_game_doesnt_have = Player.objects.exclude(id__in = game.players.all().values_list('id'))
    expansion_form = ExpansionForm()
    return render(request, 'games/detail.html', {'game': game, 'expansion_form': expansion_form, 'players': players_game_doesnt_have})

def add_expansion(request, game_id):
    form = ExpansionForm(request.POST)
    if form.is_valid():
        new_expansion = form.save(commit=False)
        new_expansion.game_id = game_id
        new_expansion.save()
    return redirect('detail', game_id=game_id)

def assoc_player(request, game_id, player_id):
    Game.objects.get(id=game_id).players.add(player_id)
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

class PlayerList(ListView):
    model = Player

class PlayerDetail(DetailView):
    model= Player

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'
