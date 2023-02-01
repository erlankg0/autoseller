from django.shortcuts import render
from django.views.generic import CreateView
from credit.forms import CreditRequestForm


class CreditRequestCreateView(CreateView):
    form_class = CreditRequestForm
    template_name = 'credit/credit.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

