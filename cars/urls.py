from django.urls import path
from cars.views import index, used_cars, taxi_cars, detail

urlpatterns = [
    path('', index, name='index'),  # main page
    path('used_cars/', used_cars, name='used_cars'),  # used cars page
    path('taxi_cars/', taxi_cars, name='taxi_cars'),  # taxi cars page
    path('detail/', detail, name='detail'),  # detail page
]
