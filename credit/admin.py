from django.contrib import admin

from credit.models import CreditRequest, TradeInRequest, Gift


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


@admin.register(TradeInRequest)
class TradeInRequestAdmin(admin.ModelAdmin):
    def get_future_car(self, obj):
        return obj.future_car

    get_future_car.short_description = 'Автомобиль на который хочет'

    def current_car(self, obj):
        text = f'{obj.current_car_brand} {obj.current_car_model} {obj.current_car_year} {obj.current_car_year} {obj.current_car_transmission}'
        return text

    current_car.short_description = 'Автомобиль который хочет продать'

    def price(self, obj):
        return f'{obj.customer_price}₽'

    price.short_description = 'Предложенная цена'

    def credit(self, obj):
        return f'{obj.credit}'

    credit.short_description = 'Кредит'

    list_display = (
        'id',
        'name',
        'phone',
        'get_future_car',
        'current_car',
        'price',
        'credit',

    )
    list_display_links = list_display
    list_filter = (
        'credit',
    )




@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    pass
