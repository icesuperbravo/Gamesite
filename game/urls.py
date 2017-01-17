from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^games/$', webshop.views.available_games),
	url(r'^games/([0-9]+)/$', game.views.gameview),
]
