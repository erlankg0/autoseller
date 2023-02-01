from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from cars.models import Model, Generation, Modification, Car, BodyType, Transmissions, Brand


class NewCarsListView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True)
        return queryset


# Detail view
class DetailCarView(DetailView):
    model = Car
    template_name = 'cars/card_detail.html'
    context_object_name = 'car'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset


def used_cars(request):
    return render(request, 'cars/used_cars.html')


def taxi_cars(request):
    return render(request, 'cars/taxi.html')


def detail(request):
    return render(request, 'cars/card_detail.html')


class CarFilterView(ListView):
    model = Car
    template_name = 'cars_filter.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        brand = self.request.GET.get('brand')
        if brand:
            queryset = queryset.filter(brand__name=brand)

        model = self.request.GET.get('model')
        if model:
            queryset = queryset.filter(model__name=model)

        generation = self.request.GET.get('generation')
        if generation:
            queryset = queryset.filter(generation__name=generation)

        year = self.request.GET.get('year')
        if year:
            queryset = queryset.filter(year__name=year)

        return queryset


# AJAX

def get_models(request):
    brand_id = request.GET.get('brand_id')
    models = Model.objects.filter(brand_id=brand_id).order_by('title').values('id', 'title')
    return JsonResponse({'models': list(models)})


def get_generations(request):
    model_id = request.GET.get('model')
    generations = Generation.objects.filter(model_id=model_id).order_by('title').values('id', 'title')
    return JsonResponse({'generations': list(generations)})


def get_modifications(request):
    generation_id = request.GET.get('generation')
    modifications = Modification.objects.filter(generation_id=generation_id).order_by('title').values('id', 'title')
    return JsonResponse({'modifications': list(modifications)})


# показать все модели автомобилей фильрации по марке, модели, поколению,
# кузову, трансмиссии, приводу, топливу, году выпуска, цене и т.д. (все поля) через Q

def get_all_cars(request):
    brand_id = Brand.objects.filter(pk=request.GET.get('brand_id'))
    model_id = Model.objects.filter(pk=request.GET.get('model_id'))
    generation_id = Generation.objects.filter(pk=request.GET.get('generation_id'))
    body_id = BodyType.objects.filter(pk=request.GET.get('body_id'))
    transmission_id = Transmissions.objects.filter(pk=request.GET.get('transmission_id'))
    drive_id = request.GET.get('drive_id')
    fuel_id = request.GET.get('fuel_id')
    year = request.GET.get('year')
    price = request.GET.get('price')
    cars = Car.objects.filter(
        Q(brand_id=brand_id) | Q(model_id=model_id) | Q(generation_id=generation_id) | Q(body_id=body_id) | Q(
            transmission_id=transmission_id) | Q(drive_id=drive_id) | Q(fuel_id=fuel_id) | Q(year=year) | Q(price=price)
    ).order_by('title').values()
    return JsonResponse({'cars': list(cars)})
