from django.http import HttpResponse, Http404
from django.shortcuts import render
from game.models import Game

def index(request):
    return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")


def about(request):
    return HttpResponse("about page")

def gameview(request, product_id):
    """A view of a single game."""
    game = Game.objects.get(pk=product_id)
    return render(request, 'game/game_view.html', {'game': game})

def available_games(request):
    """A view of all games."""
    games = Game.objects.all()
    return render(request, 'game/game_list.html', {'games': games})