from django.urls import path

from cars.views import CarsListView
from content.views import PrivacyPolicyView
from content.views import AboutView, contacts, services, insurance, feedback
from content.views import RobotsView, SitemapView

urlpatterns = [
    path('', CarsListView.as_view(), name='index'),  # main page
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('insurance/', insurance, name='insurance'),
    path('feedback/', feedback, name='feedback'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('robots/', RobotsView.as_view(), name='robots'),
    path('sitemap/', SitemapView.as_view(), name='sitemap'),
]
