from django.forms import ModelForm

from cars.models import Car, Generation, Model, TechnicalCharacteristics, Vehicle


class CarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # в поле модель добавляем только те модели, которые принадлежат выбранной марке
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['model'].queryset = Model.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = Model.objects.filter(brand_id=brand_id).order_by('title')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.models.order_by('title')

        # в поле поколение добавляем только те поколения, которые принадлежат выбранной модели
        self.fields['generation'].queryset = Generation.objects.none()

        if 'model' in self.data:
            try:
                model_id = int(self.data.get('model'))
                self.fields['generation'].queryset = Generation.objects.filter(model_id=model_id).order_by('title')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['generation'].queryset = self.instance.model.generations.order_by('title')

    class Meta:
        model = Car
        fields = (
            'brand',
            'model',
            'generation',
            'technical_characteristics',
            'color',
            'price',
            'mileage',
            'description',
            'image',
            'new',
        )
