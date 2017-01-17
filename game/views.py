from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.contrib import auth
from django.core.context_processors import csrf



def home(request):

  return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")
#
# def login(request):
#
#   return HttpResponse("Default page when not logged in.  ")

def login(request):
    c = {}
    errors=[]
    c.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request, 'home.html', {'errors': errors})
    else:
        errors.append("The username cannot be empty!")
        return render(request, 'login.html', {'c': c, 'errors': errors})

def register(request):

    return HttpResponse(" Create a new account. ")



