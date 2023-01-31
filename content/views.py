from django.shortcuts import render
from cars.models import Car


def index(request):
    cars = Car.objects.filter(new=True)
    return render(request, 'cars/index.html', {'cars': cars})


def about(request):
    return render(request, 'content/about.html')


def contacts(request):
    return render(request, 'content/contacts.html')


def insurance(request):
    return render(request, 'content/insurance.html')


def services(request):
    return render(request, 'content/services.html')


def feedback(request):
    return render(request, 'content/feedback.html')


def credit(request):
    return render(request, 'content/credit.html')
