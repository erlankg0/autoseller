from django.contrib import admin
from cars.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    list_display_links = ('title', 'icon')
    search_fields = ('title',)
