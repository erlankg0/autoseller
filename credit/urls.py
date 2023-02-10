from django.urls import path

from credit.views import CreditRequestCreateView, TradeInCreateView, callback, car_reservation, competitively
from credit.views import question
urlpatterns = [
    path('credit/', CreditRequestCreateView.as_view(), name='credit_request_create'),
    path('trade-in/', TradeInCreateView.as_view(), name='trade_in_create'),
    path('callback/', callback, name='callback'),
    path('callback/<int:pk>/', callback, name='callback'),
    path('car_reservation/', car_reservation, name='car_reservation'),
    path('competitively/', competitively, name='competitively'),
    path('question/', question, name='question'),
]
