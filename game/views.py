from django.http import HttpResponse, HttpResponseRedirect, Http404
from game.models import Game, CreateGameForm, DeleteGameForm, Profile
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
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


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
    # form = UserLoginForm()
    # if request.method == 'GET':
    #     print('GET request')
    #     return render(request, "registration/form.html", {"form":form, "title":title})
    # if request.method == 'POST':
    #     if form.is_valid():
    #         print("Login form is valid")
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return HttpResponseRedirect("/")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
            print("Login form is valid")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        print("Login form not valid")

    return render(request, "registration/form.html", {"form":form, "title":title})


def register_view(request):
    #print(request.user.is_authenticated())
    title = "Gamesite Registration"

    user_form = UserRegisterForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    print (profile_form)
    if user_form.is_valid() and profile_form.is_valid():
        print("Forms are valid")
        user = user_form.save(commit=False)
        password = user_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        profile = Profile()
        profile.user = user
        usertype = profile_form.cleaned_data.get('usertype')
        profile.usertype = usertype
        profile.save()
        if usertype == 1:
            developer_group = Group.objects.get(name='developer')
            developer_group.user_set.add(user)
            print("user into group developer")

# Email Validation
        subject = 'Congrats to you to become the newbie on Gamesite!'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email,from_email]
        contact_message = "%s via %s"%(
            user.username,
            user.email)
        some_html_message = """
        <h3>Dear user, </h3>
        <p> Congrats that you have become one of members in Gamesite Family! We warmly welcome your join!
        if you have any question or advice, please email us.</p>
        <h3> Best Regards,</h3>
        <h3> Gamesite </h3>
        """
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=True)
        messages.success(request, 'Profile details updated.')

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return HttpResponseRedirect("/")
    # else:
    #     print("Forms not valid")
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






