# from django.conf import settings
from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse, Http404, HttpResponseNotFound


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/tour.html')

# Create your views here.
