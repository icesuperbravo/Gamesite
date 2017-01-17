from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from game.models import Game, CreateGameForm, DeleteGameForm

def index(request):
    return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")


def about(request):
    return HttpResponse("about page")


def gameview(request, product_id):
    """A view of a single game."""
    game = Game.objects.get(pk=product_id)

    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)

        if form.is_valid():
            game.delete()
            return HttpResponseRedirect('/index/games/')

    else:
        form = DeleteGameForm(instance=game)

    return render(request, 'game/game_view.html', {'game': game, 'form': form})

def available_games(request):
    """A view of all games."""
    games = Game.objects.all()
    new_game = Game()
    if request.method == 'POST':
        form = CreateGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CreateGameForm(initial={'title': 'Super Django Bros.'}, instance=new_game)
    return render(request, 'game/game_list.html', {'games': games, 'form': form})