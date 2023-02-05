from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
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
        queryset = queryset.all()[0:12]
        return queryset


class NewCarsListView(ListView):
    model = Car
    template_name = 'cars/new_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True)
        queryset = queryset.filter(

        )
        return queryset


class NewCarsByBrandListView(ListView):
    model = Car
    template_name = 'cars/new_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True)
        queryset = queryset.filter(brand__id=self.kwargs['brand_id'])
        return queryset


class UsedCarsByBrandListView(ListView):
    model = Car
    template_name = 'cars/used_cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=False)
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
        context['cars'] = Car.objects.filter(price__lte=price).exclude(id=self.kwargs['pk']).order_by(
            '-price')  # будут показаны все машины с ценой ниже текущей и не будут показаны текущая машина
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


def detail(request):
    return render(request, 'cars/card_detail.html')


class CarFilterView(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(new=True)  # фильтруем по новым машинам (по умолчанию)

        my_range = self.request.GET.get('my_range')  # получаем значение из фильтра цены
        if not my_range:  # если не получили, то возвращаем все машины
            return queryset

        from_price, to_price = map(int, my_range.split(';'))  # разбиваем строку на два значения и приводим к int
        queryset = queryset.filter(price__gte=from_price, price__lte=to_price)  # фильтруем по цене

        brand = self.request.GET.get('brand')  # получаем значение из фильтра марки
        if brand:  # если получили, то фильтруем по марке и по цене &= queryset.filter(brand_id=brand)
            queryset &= queryset.filter(brand_id=brand)  # фильтруем по марке и по цене (получаем пересечение)

        model = self.request.GET.get('model')  # получаем значение из фильтра модели
        if model:  # если получили, то фильтруем по модели и по цене и по марке
            queryset &= queryset.filter(
                model_id=model)  # фильтруем по модели и по цене и по марке (получаем пересечение)

        generation = self.request.GET.get('generation')  # получаем значение из фильтра поколения
        if generation:  # если получили, то фильтруем по поколению и по цене и по марке и по модели
            queryset &= queryset.filter(
                generation_id=generation
            )  # фильтруем по поколению и по цене и по марке и по модели (получаем пересечение)

        modification = self.request.GET.get('modification')  # получаем значение из фильтра модификации
        if modification:  # если получили, то фильтруем по модификации и по цене и по марке и по модели и по поколению
            queryset &= queryset.filter(
                modification_id=modification
            )  # фильтруем по модификации и по цене и по марке и по модели и по поколению (получаем пересечение)

        year = self.request.GET.get('year')  # получаем значение из фильтра года
        if year:  # если получили, то фильтруем по году и по цене и по марке и по модели и по поколению и по модификации
            queryset &= queryset.filter(
                modification__year_id=year  # заходим в модель модификации и фильтруем по году
            )
        drive_unit = self.request.GET.get('drive_unit')  # получаем значение из фильтра привода
        if drive_unit:  # если получили, то фильтруем по приводу и по цене и по марке и по модели и по поколению и по модификации и по году
            queryset &= queryset.filter(
                modification__drive_unit_id=drive_unit  # заходим в модель модификации и фильтруем по приводу
            )
        transmission = self.request.GET.get('transmission')  # получаем значение из фильтра трансмиссии
        if transmission:  # если получили, то фильтруем по трансмиссии и по цене и по марке и по модели и по поколению и по модификации и по году и по приводу
            queryset &= queryset.filter(
                modification__transmission_id=transmission  # заходим в модель модификации и фильтруем по трансмиссии
            )

        body = self.request.GET.get('body')  # получаем значение из фильтра кузова
        if body:  # если получили, то фильтруем по кузову и по цене и по марке и по модели и по поколению и по модификации и по году и по приводу и по трансмиссии
            queryset &= queryset.filter(
                modification__body_id=body  # заходим в модель модификации и фильтруем по кузову
            )

        return queryset  # возвращаем отфильтрованный queryset (по цене, по марке, по модели, по поколению, по модификации)


def car_xml_feed(request):
    cars = Car.objects.all()
    template = get_template('cars/xml/car_xml_feed.xml')
    xml = template.render({'cars': cars})
    return HttpResponse(xml, content_type='application/xml')


def car_xml_feed_detail(request, pk):
    car = Car.objects.get(pk=pk)
    template = get_template('cars/xml/car_id_xml_feed.xml')
    xml = template.render({'car': car})
    return HttpResponse(xml, content_type='application/xml')


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
            'brand__title',
            'model__title',
            'generation__title',
            'modification__title',
            'price',
            'id',
        )
        image = CarImages.objects.filter(car_id=car_id)
        image = [i.image.url for i in image[:1]]
        # добавить картинки в словарь
        result = list(car)
        result[0]['image'] = image[0]
        return JsonResponse({'car': result})
