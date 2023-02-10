from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cars.models import Car
from credit.forms import CreditRequestForm
from credit.models import TradeIn, CallBack, TradeInRequest, CarReservation


class CreditRequestCreateView(CreateView):
    form_class = CreditRequestForm
    template_name = 'credit/credit.html'
    success_url = reverse_lazy('credit_request_create')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ваша заявка на кредит успешно отправлена")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Ваша заявка на кредит не отправлена")
        return super().form_invalid(form)


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
    model = TradeInRequest
    fields = '__all__'
    success_url = reverse_lazy('trade_in_create')
    template_name = 'credit/taxi.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ваша заявка на Trade-in успешно отправлена")
        print(
            f"Заявка на Trade-in от {form.cleaned_data['name']} с номером телефона {form.cleaned_data['phone']}"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Ваша заявка на Trade-in не отправлена")
        return super().form_invalid(form)


def callback(request):
    if request.method == 'GET':
        CallBack.objects.create(
            name=request.GET.get('name'),
            phone=request.GET.get('phone'),
        )
    return redirect('index')


def car_reservation(request):
    if request.method == 'GET':
        car = Car.objects.get(id=request.GET.get('pk'))
        CarReservation.objects.create(
            car=car,
            name=request.GET.get('name'),
            phone=request.GET.get('phone'),

        )
    return redirect('index')
