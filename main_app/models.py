from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    relyear = models.IntegerField()

def __str__(self):
    return f'{self.title} ({self.id})'




