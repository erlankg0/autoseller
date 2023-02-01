from django.forms import ModelForm

from cars.models import Car, Generation, Model, Modification


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
