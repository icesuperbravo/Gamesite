from django.conf.urls import url

from . import views

urlpatterns = [

    #URL for getting JSON data for a given continent code (ex 7.2)
    url(r'^(\w{2}).json$', views.continent_json, name='continent-json'),

    # URL for getting JSON data for a given country codes (in given continent) (ex 7.2)
    url(r'^(\w{2})/(\w{2}).json$', views.country_json, name='country-json'),
]
