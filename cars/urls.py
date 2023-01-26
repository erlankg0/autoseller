from django.urls import path
from cars.views import index

urlpatterns = [
    path('', index, name='index'),  # main page
    path('used_cars/', index, name='used_cars'),  # used cars page
    path('taxi_cars/', index, name='taxi_cars'),  # taxi cars page
]
