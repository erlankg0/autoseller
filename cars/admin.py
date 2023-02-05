from django.contrib import admin

from cars.forms import CarForm
from cars.models import Brand, Model, Generation, Modification, Kitting
from cars.models import Car, CarImages
from cars.models import Engine, Transmissions, DriveUnit, Fuel, BodyType, Years, Volume


@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
    pass


@admin.register(Kitting)
class KittingAdmin(admin.ModelAdmin):
    pass


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    pass


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    pass


@admin.register(Transmissions)
class TransmissionsAdmin(admin.ModelAdmin):
    pass


@admin.register(DriveUnit)
class DriveUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    pass


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    pass


@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    pass


class CarImagesAdmin(admin.StackedInline):
    model = CarImages
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    form = CarForm
    inlines = [CarImagesAdmin]

    def get_brand(self, obj):
        return obj.brand.title

    def get_model(self, obj):
        return obj.model.title

    def get_generation(self, obj):
        return obj.generation.title

    def get_year(self, obj):
        return obj.modification.year

    def get_modification(self, obj):
        return obj.modification.title

    list_display = ('new', 'get_brand', 'get_model', 'get_generation', 'price', 'get_year', 'get_modification')
    list_display_links = ('get_brand', 'get_model', 'get_generation', 'get_year', 'get_modification')
    list_editable = ('price', 'new',)
    list_filter = ('price', 'mileage',)
