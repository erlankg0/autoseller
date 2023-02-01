from django.urls import path

from cars.views import DetailCarView
from cars.views import get_models, get_generations, get_modifications, get_all_cars
from cars.views import used_cars, taxi_cars, detail

urlpatterns = [
    path('cars/detailed/<int:pk>/', DetailCarView.as_view(), name='car_detail'),
    path('used_cars/', used_cars, name='used_cars'),  # used cars page
    path('taxi_cars/', taxi_cars, name='taxi_cars'),  # taxi cars page
    path('detail/', detail, name='detail'),  # detail page
    # AJAX requests
    path('get_models/', get_models, name='get_models'),
    path('get_generations/', get_generations, name='get_generations'),
    path('get_modifications/', get_modifications, name='get_modifications'),
    path('get_all_cars/', get_all_cars, name='get_all_cars'),
]
