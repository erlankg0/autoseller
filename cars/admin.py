from django.contrib import admin
from cars.models import Brand, Vehicle, Car, Generation, Model


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
    pass
