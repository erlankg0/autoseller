from django.urls import path

from credit.views import CreditRequestCreateView, TradeInCreateView, callback

urlpatterns = [
    path('credit/', CreditRequestCreateView.as_view(), name='credit_request_create'),
    path('trade-in/', TradeInCreateView.as_view(), name='trade_in_create'),
    path('callback/', callback, name='callback'),
]
