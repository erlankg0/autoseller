from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView

from credit.forms import CreditRequestForm
from credit.models import TradeIn


class CreditRequestCreateView(CreateView):
    form_class = CreditRequestForm
    template_name = 'credit/credit.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def trade_in(request):
    trade_in, created = TradeIn.objects.get_or_create(
        name=request.GET.get('name'),
        phone=request.GET.get('phone'),
    )
    if created:
        messages.success(request, "Ваша заявка принята на Trade-in успешно отправлена")
    else:
        messages.warning(request, "Вы уже отправляли заявку на Trade-in")
    return redirect('/')


class TradeInCreateView(CreateView):
    model = TradeIn
    fields = ['name', 'phone']
    success_url = '/'
    template_name = 'credit/taxi.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
