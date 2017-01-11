from django.http import HttpResponse


def index(request):


  return HttpResponse("Default page when logged in. As a player, see the overview of your profile, games owned, and highscores.  ")
