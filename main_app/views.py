from django.shortcuts import render

class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, platform, description, relyear):
    self.title = title
    self.platform = platform
    self.description = description
    self.relyear = relyear

games = [
  Game('Fallout: New Vegas', 'PC', 'Fantastic', 2010),
  Game('Deus Ex: Human Revolution', 'PC', 'Fantastic', 2011),
  Game('Witcher 3: Wild Hunt', 'PC', 'Great', 2015)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {'games': games})


