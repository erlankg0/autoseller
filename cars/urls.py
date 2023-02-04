from django.urls import path

from cars.views import DetailCarView, UsedCarsListView, NewCarsByBrandListView, UsedCarsByBrandListView, NewCarsListView
from cars.views import detail
from cars.views import get_models, get_generations, get_modifications, get_all_cars, get_cars_by_model, get_car

urlpatterns = [
    path('new/brand/<int:brand_id>/', NewCarsByBrandListView.as_view(), name='brand_new'),
    path('used/brand/<int:brand_id>/', UsedCarsByBrandListView.as_view(), name='brand_old'),
    path('detailed/<int:pk>/', DetailCarView.as_view(), name='car_detail'),
    path('new_cars/', NewCarsListView.as_view(), name='new_cars'),  # new cars page
    path('used_cars/', UsedCarsListView.as_view(), name='used_cars'),  # used cars page
    path('detail/', detail, name='detail'),  # detail page
    # AJAX requests
    path('get_models/', get_models, name='get_models'),
    path('get_generations/', get_generations, name='get_generations'),
    path('get_modifications/', get_modifications, name='get_modifications'),
    path('get_all_cars/', get_all_cars, name='get_all_cars'),
    path('get_cars_by_model/', get_cars_by_model, name='get_cars_by_model'),
    path('get_car/', get_car, name='get_car'),
]
