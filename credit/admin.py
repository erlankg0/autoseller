from django.contrib import admin
from credit.models import CreditRequest


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
