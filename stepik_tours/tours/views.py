# from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def custom_handler404(request, exception):
    return HttpResponseNotFound("Ресурс не найден!")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка сервера!")


def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    return render(request, "tours/departure.html")


def tour_view(request, id):
    return render(request, "tours/tour.html")


# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'tours/index.html')


# class DepartureView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'tours/departure.html')


# class TourView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'tours/tour.html')

# Create your views here.
