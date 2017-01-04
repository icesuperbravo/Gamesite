from django.conf.urls import url

from . import views

urlpatterns = [

    # URL for getting HTML page with list of continents (ex 7.3)
    url(r"^$", views.show_continent, name='continent-all'),

    # URL for getting HTML partial page for a given continent (ex 7.3)
    url(r"^(\w{2}).html$", views.show_continent, name='continent-details'),
]
