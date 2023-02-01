from django.urls import path
from credit.views import CreditRequestCreateView

urlpatterns = [
    path('credit/', CreditRequestCreateView.as_view(), name='credit_request_create'),
]
