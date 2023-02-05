from django.contrib.syndication.views import Feed
from django.urls import reverse

from cars.models import Car


class CarFeed(Feed):
    title = "Car Feed"
    link = "/feed/"
    description = "Updates on new and used cars for sale"

    def items(self):
        return Car.objects.all()

    def item_title(self, item):
        return item.__str__()

    def item_description(self, item):
        return item.description

    def item_brand(self, item):
        return item.brand.title

    def item_model(self, item):
        return item.model.title

    def item_price(self, item):
        return item.price

    def item_mileage(self, item):
        return item.mileage

    def item_modification(self, item):
        return item.modification

    def item_link(self, item):
        return reverse('car_detail', args=[str(item.id)])

    def item_credit(self, item):
        return item.credit


class CarDetailFeed(Feed):
    def get_object(self, request, pk):
        return Car.objects.get(pk=pk)

    def title(self, obj):
        return "Car detail feed for %s" % obj.__str__()

    def description(self, obj):
        return obj.description

    def item_brand(self, item):
        return item.brand.title

    def item_model(self, item):
        return item.model.title

    def link(self, obj):
        return reverse('car_detail', args=[str(obj.id)])

    def items(self, obj):
        return [obj]

    def item_title(self, item):
        return item.__str__()

    def item_description(self, item):
        return item.__str__()
