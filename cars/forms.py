from django.forms import ModelForm

from cars.models import Car, Generation, Model, Modification


class CarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # в поле модель добавляем только те модели, которые принадлежат выбранной марке
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['model'].queryset = Model.objects.none()

        if 'brand' in self.data:  # если в форме выбрана марка авто (поле brand)
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
        self.fields['modification'].queryset = Modification.objects.none()

        if 'generation' in self.data:
            try:
                generation_id = int(self.data.get('generation'))
                self.fields['modification'].queryset = Modification.objects.filter(
                    generation_id=generation_id).order_by('title')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['modification'].queryset = self.instance.generation.modifications.order_by('title')

    class Meta:
        model = Car
        fields = '__all__'
