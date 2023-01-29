from django.urls import path
from content.views import about, contacts, services, insurance, index, feedback, credit

urlpatterns = [
    path('', index, name='index'),  # main page
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('insurance/', insurance, name='insurance'),
    path('feedback/', feedback, name='feedback'),
    path('credit/', credit, name='credit'),
]
