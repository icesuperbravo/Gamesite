"""gamesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from game.views import *
# from game.urls import *

urlpatterns = [
    # url('^', include('django.contrib.auth.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^$', available_games, name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('', include('social_django.urls', namespace='social')),
    # url(r'^register/$', CreateView.as_view(
    #     template_name='registration/register.html',
    #     form_class=UserCreationForm,
    #     success_url='home'
    # )),


    url(r'^games/$', available_games, name='game_lists'),
    url(r'^games/([0-9]+)/$', game_view, name='single_game'),
    url(r'^games/([0-9]+)/buy/$', game_buy_view, name = 'buy_game'),
    url(r'^test/', test),

    url(r'^developer/$', developer_view),
    url(r'^developer/([0-9]+)/$', developer_public_view),

    url(r'^payment/cancel', payment_cancel_view, name= 'payment_cancel'),
    url(r'^payment/success', payment_success_view, name= 'payment_success'),
    url(r'^payment/error/([0-9]+)/$', payment_error_view, name= 'payment_error'),
    #url(r'^payment/existed_games', payment_error_view, name= 'payment_success'),


]


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
