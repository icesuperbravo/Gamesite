from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import  UserLoginForm, UserRegisterForm


def home(request):

  return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")

def login_view(request):
    title ="Gamesite Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

    return render(request, "registration/form.html", {"form":form, "title":title})

def register_view(request):
    print(request.user.is_authenticated())
    title = "Gamesite Registeration"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return HttpResponseRedirect("/")
    return render(request, "registration/form.html",  {"form":form, "title":title})

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






