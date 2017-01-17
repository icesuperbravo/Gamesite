from django.http import HttpResponse, Http404
from django.shortcuts import render
from game.models import Game, GameForm

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
    new_game = Game()
    form = GameForm(initial={'title': 'Super Django Bros.'}, instance=new_game)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = GameForm()
    return render(request, 'game/game_list.html', {'games': games, 'form': form})