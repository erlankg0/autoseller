from django.http import JsonResponse
from django.shortcuts import render
from cars.models import Brand, Model, Generation, Car, TechnicalCharacteristics, CarImages


def used_cars(request):
    return render(request, 'cars/used_cars.html')


def taxi_cars(request):
    return render(request, 'cars/taxi.html')


def detail(request):
    return render(request, 'cars/card_detail.html')


# AJAX

def get_models(request):
    brand_id = request.GET.get('brand_id')
    models = Model.objects.filter(brand_id=brand_id).order_by('title').values('id', 'title')
    return JsonResponse({'models': list(models)})


def get_generations(request):
    model_id = request.GET.get('model')
    generations = Generation.objects.filter(model_id=model_id).order_by('title').values('id', 'title')
    return JsonResponse({'generations': list(generations)})
