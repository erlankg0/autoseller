from django.urls import path
from content.views import about, contacts, services, insurance, feedback, credit
from cars.views import NewCarsListView

urlpatterns = [
    path('', NewCarsListView.as_view(), name='index'),  # main page
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('insurance/', insurance, name='insurance'),
    path('feedback/', feedback, name='feedback'),
    path('credit/', credit, name='credit'),
]
