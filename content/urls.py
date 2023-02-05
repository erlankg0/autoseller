from django.urls import path

from cars.views import CarsListView
from content.views import PrivacyPolicyView
from content.views import about, contacts, services, insurance, feedback

urlpatterns = [
    path('', CarsListView.as_view(), name='index'),  # main page
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('insurance/', insurance, name='insurance'),
    path('feedback/', feedback, name='feedback'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
]
