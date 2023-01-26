from django.shortcuts import render


def index(request):
    return render(request, 'cars/index.html')


def used_cars(request):
    return render(request, 'cars/index.html')


def taxi_cars(request):
    return render(request, 'cars/index.html')
