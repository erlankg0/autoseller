from django.contrib import admin
from cars.models import Engine, Transmissions, DriveUnit, Fuel, BodyType, Years, Volume
from cars.models import Brand, Model, Generation, Modification
from cars.models import Car, CarImages
from cars.forms import CarForm


@admin.register(Years)
class YearsAdmin(admin.ModelAdmin):
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
