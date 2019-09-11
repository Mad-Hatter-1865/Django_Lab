from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Player
from .forms import ExpansionForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'gamecollector'

import uuid
import boto3
from .models import Game, Player, Photo



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

def add_photo(request, game_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, game_id=cat_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', game_id=cat_id)

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
