import datetime

from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.views.generic import ListView, DetailView

from cars.models import Model, Generation, Modification, Car, CarImages


class CarsListView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class NewCarsListView(ListView):
    model = Car
    template_name = 'cars/new_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True, is_active=True)
        return queryset


class NewCarsByBrandListView(ListView):
    model = Car
    template_name = 'cars/new_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True, is_active=True) # new=True, is_active=True - это дефолтные значения
        queryset = queryset.filter(brand__id=self.kwargs['brand_id'])
        return queryset


class UsedCarsByBrandListView(ListView):
    model = Car
    template_name = 'cars/used_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=False, is_active=True)
        queryset = queryset.filter(brand__id=self.kwargs['brand_id'])
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        price = Car.objects.get(id=self.kwargs['pk']).price
        context['olds'] = Car.objects.filter(price__lte=price).exclude(id=self.kwargs['pk'])[:4]
        return context


class UsedCarsListView(ListView):
    model = Car
    template_name = 'cars/used_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=False)
        return queryset


def car_xml_feed(request):
    cars = Car.objects.all()
    template = get_template('cars/xml/car_xml_feed.xml')
    # get current date time
    date = datetime.datetime.now()
    xml = template.render({'cars': cars, "data": date.strftime("%Y-%m-%d %H:%M:%S")})
    return HttpResponse(xml, content_type='application/xml')


def car_xml_feed_detail(request, pk):
    car = Car.objects.get(pk=pk)
    template = get_template('cars/xml/car_id_xml_feed.xml')
    xml = template.render({'car': car})
    return HttpResponse(xml, content_type='application/xml')


# AJAX

def get_car_by_pk(request):
    car = Car.objects.get(pk=request.GET.get('pk'))
    image = [image.image.url for image in car.car_images.all()[:1]]
    return JsonResponse({
        'brand': car.brand.title,
        'model': car.model.title,
        'generation': car.generation.title,
        'modification': car.modification.title,
        'price': car.price,
        'image': image,
    })


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
    print(generation_id)
    modifications = Modification.objects.filter(generation_id=generation_id).order_by('title').values('id', 'title')
    return JsonResponse({'modifications': list(modifications)})


def get_cars_by_model(request):
    model = request.GET.get('model')
    cars = Car.objects.filter(model_id=model).order_by('price').values(
        'brand__title',
        'model__title',
        'generation__title',
        'modification__title',
        'price',
        'id',

    )
    return JsonResponse({'cars': list(cars)})


def get_car(request):
    car_id = request.GET.get('car')
    if car_id != '':
        car = Car.objects.filter(id=car_id).values(

        )
        images = [image.image.url for image in Car.objects.get(id=car_id).car_images.all()]
        result = list(car)
        result[0]['images'] = images
        return JsonResponse({'car': result})
