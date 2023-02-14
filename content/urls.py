from django.urls import path

from cars.views import CarsListView
from content.views import PrivacyPolicyView
from content.views import AboutView, contacts, services, insurance, feedback
from content.views import RobotsView, SitemapView
from django.views.generic import TemplateView
urlpatterns = [
    path('', CarsListView.as_view(), name='index'),  # main page
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('insurance/', insurance, name='insurance'),
    path('feedback/', feedback, name='feedback'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('sitemap/', SitemapView.as_view(), name='sitemap'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
]
