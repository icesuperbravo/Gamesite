from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
	url(r'^games/$', views.available_games),
	url(r'^games/([0-9]+)/$', views.gameview),
]
