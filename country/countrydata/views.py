from django.http import Http404
from django.http import HttpResponse
import json

from .models import Continent, Country


def continent_json(request, continent_code):
    """ Write your answer in 7.2 here. """
    try:
        continent = Continent.objects.get(code = continent_code)
    except Continent.DoesNotExist:
        raise Http404

    callback = request.GET.get('callback', 'empty')

    temp = {}
    for country in continent.countries.all():
        temp[country.code] = country.name

    if(callback == 'empty'):
        return HttpResponse(json.dumps(temp), content_type="application/json")
    else:
        return HttpResponse(callback + '(' + json.dumps(temp) + ')', content_type="application/json")


def country_json(request, continent_code, country_code):
    """ Write your answer in 7.2 here. """
    try:
         continent = Continent.objects.get(code = continent_code)
         country = continent.countries.get(code = country_code)
         
    except Country.DoesNotExist:
        raise Http404
    except Continent.DoesNotExist:
        raise Http404
    callback = request.GET.get('callback', 'empty')

    temp = {"area" : country.area, "population" : country.population, "capital" : country.capital}


    if(callback == 'empty'):
        return HttpResponse(json.dumps(temp), content_type="application/json")
    else:
        return HttpResponse(callback + '(' + json.dumps(temp) + ')', content_type="application/json")
