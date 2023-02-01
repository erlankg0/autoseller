from django import forms
from credit.models import CreditRequest


class CreditRequestForm(forms.ModelForm):
    class Meta:
        model = CreditRequest
        fields = (
            'brand',
            'model',
            'car',
            'name',
            'initial_payment',
            'credit_term',
            'phone',
            'is_checked',
        )
