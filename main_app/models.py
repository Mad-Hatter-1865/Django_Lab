from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})

class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    relyear = models.IntegerField()
    players = models.ManyToManyField(Player)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

class Expansion(models.Model):
    extitle = models.CharField(max_length=100)
    rely = models.IntegerField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"
