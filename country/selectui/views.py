from django.shortcuts import render, get_object_or_404

from countrydata.models import Continent


def show_continent(request, continent_code=None):
    context = {
        "all_continents": Continent.objects.all()
    }
    if continent_code:
        continent = get_object_or_404(Continent, code=continent_code)
        context["continent"] = continent

    # Add your answer in 7.3 here
    return render(request, "selectui/index.html", context)
