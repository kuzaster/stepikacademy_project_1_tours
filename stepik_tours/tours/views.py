import random

from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

import data

# Create your views here.


def custom_handler404(request, exception):
    return HttpResponseNotFound("Ресурс не найден!")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка сервера!")


def main_view(request):
    keys = random.sample(list(data.tours), 6)
    tours = {key: data.tours[key] for key in keys}
    return render(request, "tours/index.html", {"data": data, "tours": tours})


def departure_view(request, departure):
    tours = {
        key: value
        for key, value in data.tours.items()
        if value["departure"] == departure
    }
    depart = data.departures[departure]
    costs = sorted((tour["price"] for tour in tours.values()))
    nights = sorted((tour["nights"] for tour in tours.values()))
    return render(
        request,
        "tours/departure.html",
        {
            "tours": tours,
            "data": data,
            "departure": depart,
            "costs": costs,
            "nights": nights,
        },
    )


def tour_view(request, id):
    tour = data.tours[id]
    departure = data.departures[tour["departure"]]
    stars = "★" * int(tour["stars"])
    return render(
        request,
        "tours/tour.html",
        {"tour": tour, "departure": departure, "stars": stars, "data": data},
    )
