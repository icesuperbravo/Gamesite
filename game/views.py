from django.http import HttpResponse, HttpResponseRedirect, Http404
from game.models import Game, CreateGameForm, DeleteGameForm
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import  UserLoginForm, UserRegisterForm, ProfileForm


def index(request):
    return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")

def home(request):
  return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")


def about(request):
    return HttpResponse("about page")

@login_required()
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

def login_view(request):
    title ="Gamesite Login"
    print("Login view")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
            print("Login form is valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
    else:
        print("Login form not valid")

    return render(request, "registration/form.html", {"form":form, "title":title})

def register_view(request):
    #print(request.user.is_authenticated())
    title = "Gamesite Registeration"
    user_form = UserRegisterForm(request.POST or None)
    # = UserForm(request.POST, instance=request.user)

    if request.user.is_anonymous():
        profile_form = ProfileForm(request.POST or None)
    else:
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
        print("Forms are valid")
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        print("Saved user")
        # profile_form.save()
        # print("Saved profile")
        new_user = authenticate(username=user.username, password=password)
        print("Logging in")
        login(request, new_user)
        print("Redirecting")
        return HttpResponseRedirect("/")
    else:
        print("Forms not valid")
    return render(request, "registration/form.html",  {"user_form":user_form, "profile_form":profile_form, "title":title})

def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html", {})




@login_required()
def test(request):

    if request.user.is_authenticated:
        print(request.user)
        return HttpResponse("url authenticated")
    else:
        return HttpResponse("failure")






