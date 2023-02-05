from django.shortcuts import render
from django.views import View


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'content/privacy.html')


def about(request):
    return render(request, 'content/about.html')


def contacts(request):
    return render(request, 'content/contacts.html')


def insurance(request):
    return render(request, 'content/insurance.html')


def services(request):
    return render(request, 'content/services.html')


def feedback(request):
    return render(request, 'content/feedback.html')

