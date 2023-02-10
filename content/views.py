from django.shortcuts import render
from django.views.generic import TemplateView

from cars.models import Car, CarImages
from cars.models import Exterior, Interior, Comfort, Secure, Other
from cars.models import Brand, Model, Generation, Modification
from cars.models import Engine, Transmissions, DriveUnit, BodyType
from content.models import About


class PrivacyPolicyView(TemplateView):
    template_name = 'content/privacy.html'


class RobotsView(TemplateView):
    template_name = 'content/robots.txt'
    content_type = 'text/plain'  # this is important! It tells the browser that this is a text file


class SitemapView(TemplateView):
    template_name = 'content/sitemap.xml'
    content_type = 'application/xml'  # this is important! It tells the browser that this is a text file

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'content/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context


def contacts(request):
    return render(request, 'content/contacts.html')


def insurance(request):
    return render(request, 'content/insurance.html')


def services(request):
    return render(request, 'content/services.html')


def feedback(request):
    return render(request, 'content/feedback.html')
