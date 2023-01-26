from django.shortcuts import render


def index(request):
    return render(request, 'cars/index.html')


def used_cars(request):
    return render(request, 'cars/used_cars.html')


def taxi_cars(request):
    return render(request, 'cars/taxi.html')


def detail(request):
    return render(request, 'cars/card_detail.html')
