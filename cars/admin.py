from django.contrib import admin

from cars.forms import CarForm
from cars.models import Brand, Model, Generation, Modification, Kitting
from cars.models import Car, CarImages
from cars.models import Engine, Transmissions, DriveUnit, Fuel, BodyType, Years, Volume
from cars.models import Exterior, Interior, Secure, Comfort, Multimedia, Other


@admin.register(Exterior)
class ExteriorAdmin(admin.ModelAdmin):
    pass


@admin.register(Interior)
class InteriorAdmin(admin.ModelAdmin):
    pass


@admin.register(Secure)
class SecureAdmin(admin.ModelAdmin):
    pass


@admin.register(Comfort)
class ComfortAdmin(admin.ModelAdmin):
    pass


@admin.register(Multimedia)
class MultimediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    pass


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

    get_year.short_description = 'Год'
    get_brand.short_description = 'Марка'
    get_model.short_description = 'Модель'
    get_generation.short_description = 'Поколение'
    get_modification.short_description = 'Модификация'

    list_display = (
    'new', 'is_active', 'get_brand', 'get_model', 'get_generation', 'price', 'get_year', 'get_modification')
    list_display_links = ('get_brand', 'get_model', 'get_generation', 'get_year', 'get_modification')
    list_editable = ('price', 'new', 'is_active')
    list_filter = ('new', 'is_active', 'brand', 'price',)
