from django.contrib import admin
from cars.models import Brand, Vehicle, Car, Generation, Model, TechnicalCharacteristics, CarImages
from cars.forms import CarForm


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    list_display_links = ('title', 'icon')
    search_fields = ('title',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = list_display


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarForm

    def get_brand(self, obj):
        return obj.model.brand.title

    def get_model(self, obj):
        return obj.model.title

    def get_generation(self, obj):
        return obj.generation.title

    get_brand.short_description = 'Бренд'
    get_model.short_description = 'Модель'
    get_generation.short_description = 'Поколение'

    list_display = (
        'get_brand',
        'get_model',
        'get_generation',
        'price',
        "new",
    )
    list_display_links = list_display



@admin.register(TechnicalCharacteristics)
class TechnicalCharacteristicsAdmin(admin.ModelAdmin):
    pass


@admin.register(CarImages)
class CarImagesAdmin(admin.ModelAdmin):
    pass
