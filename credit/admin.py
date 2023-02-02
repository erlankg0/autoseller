from django.contrib import admin
from credit.models import CreditRequest, TradeIn


@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'brand',
        'model',
        'car',
        'name',
        'initial_payment',
        'credit_term',
        'phone',
        'is_checked',
    )
    list_display_links = (
        'id',
        'brand',
        'model',
        'car',
        'name',
        'initial_payment',
        'credit_term',
        'phone',
        'is_checked',
    )
    list_filter = (
        'brand',
        'model',
        'car',
        'name',
        'initial_payment',
        'credit_term',
        'phone',
        'is_checked',
    )
    search_fields = (
        'brand',
        'model',
        'car',
        'name',
        'initial_payment',
        'credit_term',
        'phone',
        'is_checked',
    )
    list_per_page = 20


@admin.register(TradeIn)
class TradeInAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone',
    )
    list_display_links = (
        'id',
        'name',
        'phone',
    )
    list_filter = (
        'name',
        'phone',
    )
    search_fields = (
        'name',
        'phone',
    )
    list_per_page = 20 # пагинация по 20 записей на странице
