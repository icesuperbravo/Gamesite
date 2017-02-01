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
    url(r'^$', home, name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url('', include('social_django.urls', namespace='social')),

    # url(r'^register/$', CreateView.as_view(
    #     template_name='registration/register.html',
    #     form_class=UserCreationForm,
    #     success_url='home'
    # )),


    url(r'^games/$', available_games, name='available_games'),
    url(r'^games/([0-9]+)/$', gameview),
    url(r'^test/', test),


]


# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
