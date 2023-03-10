from django import forms

from credit.models import CreditRequest, TradeIn, CallBack, TradeInRequest


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


class TradeInForm(forms.ModelForm):
    class Meta:
        model = TradeIn
        fields = (
            "name",
            "phone",
        )


class TradeInRequestForm(forms.ModelForm):
    class Meta:
        model = TradeInRequest
        fields = '__all__'


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = (
            "name",
            "phone",
        )
