from django.urls import path
from credit.views import CreditRequestCreateView, trade_in

urlpatterns = [
    path('credit/', CreditRequestCreateView.as_view(), name='credit_request_create'),
    path('trade-in/', trade_in, name='trade_in_create'),
]
