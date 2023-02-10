from django.urls import path

from cars.feed import CarFeed, CarDetailFeed
from cars.views import DetailCarView, UsedCarsListView, NewCarsByBrandListView, UsedCarsByBrandListView
from cars.views import NewCarsListView, car_xml_feed, car_xml_feed_detail
from cars.views import get_models, get_generations, get_modifications, get_cars_by_model, get_car, get_car_by_pk

urlpatterns = [
    path('new/brand/<int:brand_id>/', NewCarsByBrandListView.as_view(), name='brand_new'),
    path('used/brand/<int:brand_id>/', UsedCarsByBrandListView.as_view(), name='brand_old'),
    path('detailed/<int:pk>/', DetailCarView.as_view(), name='car_detail'),
    path('new_cars/', NewCarsListView.as_view(), name='new_cars'),  # new cars page
    path('used_cars/', UsedCarsListView.as_view(), name='used_cars'),  # used cars page
    # AJAX requests
    path('get_models/', get_models, name='get_models'),
    path('get_generations/', get_generations, name='get_generations'),
    path('get_modifications/', get_modifications, name='get_modifications'),
    path('get_cars_by_model/', get_cars_by_model, name='get_cars_by_model'),
    path('get_car/', get_car, name='get_car'),
    path('get_car_by_pk/', get_car_by_pk, name='get_car_by_pk'),
    # FEED
    path('feed/', CarFeed(), name='car_feed'),
    path('car_xml_feed/', car_xml_feed, name='car_xml_feed'),
    path('car_xml_feed_detail/<int:pk>/', car_xml_feed_detail, name='car_xml_feed_detail'),
    path('<int:pk>/feed/', CarDetailFeed(), name='car_detail_feed'),
]
