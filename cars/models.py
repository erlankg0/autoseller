from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from cars.utils import directory_image_path, directory_image_path_vehicle


class Engine(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название двигателя',
        help_text='Наименование двигателя (например, M20B25)',
        unique=True,
    )
    fuel = models.ForeignKey(
        'Fuel',
        on_delete=models.CASCADE,
        verbose_name='Тип топлива',
        help_text='Тип топлива (например, Бензин)',
    )

    def __str__(self):
        return "%s %s" % (self.title, self.fuel)

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Типы двигателей'
        db_table = 'engine'


class Transmissions(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Трансмиссия',
        help_text='Трансмиссия автомобиля (например, Автомат)',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Трансмиссии'
        db_table = 'transmissions'


class DriveUnit(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Привод',
        help_text='Привод автомобиля (например, Передний)',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Привод'
        db_table = 'drive'


class Fuel(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Топливо',
        help_text='Топливо автомобиля (например, Бензин)',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Топливо'
        verbose_name_plural = 'Топливо'
        db_table = 'fuel'


class Volume(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Объем двигателя',
        help_text='Объем двигателя автомобиля (например, 2.0)',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объем двигателя'
        verbose_name_plural = 'Объем двигателя'
        db_table = 'volume'


class Years(models.Model):
    title = models.DateField(
        verbose_name='Год выпуска',
        help_text='Год выпуска автомобиля (например, 2019)',
        unique=True,
    )

    def __str__(self):
        return f'{self.title.year}'

    class Meta:
        verbose_name = 'Год выпуска'
        verbose_name_plural = 'Год выпуска'
        db_table = 'years'


class BodyType(models.Model):  # Тип кузова  (например, Седан) и иконка типа кузова
    title = models.CharField(
        verbose_name='Тип транспорта',
        help_text='Пример (Седан.)',
        max_length=100,
        unique=True,
    )
    image = models.ImageField(
        upload_to=directory_image_path_vehicle,
        verbose_name="Изображения транспорта",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип транспорта'
        verbose_name_plural = 'Типы транспортов'
        db_table = "vehicle"


# Модель марки автомобиля (например, BMW) и иконка марки автомобиля
class Brand(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Марка',
        help_text='Марка автомобиля (например, BMW)',
        unique=True,
    )
    icon = models.ImageField(
        upload_to=directory_image_path,
        verbose_name='Иконка',
        help_text='Иконка марки автомобиля',
        blank=True,
        null=True,
    )

    # get all cars of this brand which new=True
    def get_new_cars(self):
        # which new=True
        return reverse('brand_new', kwargs={'brand_id': self.id})

    def get_old_cars(self):
        return reverse('brand_old', kwargs={'brand_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['title']
        db_table = 'brands'


# Модель (например, BMW X5)
class Model(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Модель',
        help_text='Модель автомобиля (например, BMW X5)',
        unique=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Марка',
        help_text='Марка автомобиля',
        related_name='models',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['title']
        db_table = 'models'


# Поколение автомобиля
class Generation(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Поколение',
        help_text='Поколение автомобиля (например, 2019)',
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        verbose_name='Модель',
        help_text='Модель автомобиля',
        related_name='generations',
        # related_name='generations' - это имя для обратной связи
    )

    def __str__(self):
        return f"{self.model} {self.title}"

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'
        ordering = ['title']
        db_table = 'generations'


class Modification(models.Model):
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        verbose_name='Модель',
        help_text='Модель автомобиля (например, 3 серия)',
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Модификация',
        help_text='Модификация автомобиля (например, 320i)',
        unique=True,
    )
    engine = models.ForeignKey(
        Engine,
        on_delete=models.CASCADE,
        verbose_name='Двигатель',
        help_text='Двигатель автомобиля',
        related_name='engine_modifications',
    )
    power = models.CharField(
        max_length=50,
        verbose_name='Мощность',
        help_text='Мощность двигателя автомобиля',
    )
    fuel_consumption = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Расход топлива',
        help_text='Расход топлива автомобиля (5.3)',
        blank=True,
        null=True,
    )
    max_speed = models.PositiveIntegerField(
        verbose_name='Максимальная скорость',
        help_text='Максимальная скорость автомобиля (250)',
        blank=True,
        null=True,
    )
    acceleration = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Разгон до 100 км/ч',
        help_text='Разгон до 100 км/ч автомобиля (5.3)',
        blank=True,
        null=True,
    )
    volume = models.ForeignKey(
        Volume,
        on_delete=models.CASCADE,
        verbose_name='Объем двигателя',
        help_text='Объем двигателя автомобиля',
        related_name='volume_modifications',
    )
    transmission = models.ForeignKey(
        Transmissions,
        on_delete=models.CASCADE,
        verbose_name='Коробка передач',
        help_text='Коробка передач автомобиля',
        related_name='transmission_modifications',
    )
    drive_unit = models.ForeignKey(
        DriveUnit,
        on_delete=models.CASCADE,
        verbose_name='Привод',
        help_text='Привод автомобиля',
        related_name='drive_unit_modifications',
    )
    body_type = models.ForeignKey(
        BodyType,
        on_delete=models.CASCADE,
        verbose_name='Тип кузова',
        help_text='Тип кузова автомобиля',
        related_name='body_type_modifications',
    )
    year = models.ForeignKey(
        Years,
        on_delete=models.CASCADE,
        verbose_name='Год выпуска',
        help_text='Год выпуска автомобиля',
        related_name='year_modifications',
    )

    def __str__(self):
        return f"{self.model} {self.title}"

    class Meta:
        verbose_name = 'Модификация'
        verbose_name_plural = 'Модификации'
        db_table = 'modification'


class Kitting(models.Model):  # Комплектация автомобиля
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Название опции (салон)',
    )
    description = models.CharField(
        max_length=50,
        verbose_name='Описание опция',
        help_text='Описание опции (кожа)',
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'
        db_table = 'kitting'


class Secure(models.Model):  # Безопасность автомобиля
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Безопасность'
        verbose_name_plural = 'Безопасности'
        db_table = 'secure'


class Exterior(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Экстерьер'
        verbose_name_plural = 'Экстерьеры'
        db_table = 'exterior'


class Interior(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интерьер'
        verbose_name_plural = 'Интерьеры'
        db_table = 'interior'


class Comfort(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комфорт'
        verbose_name_plural = 'Комфорты'
        db_table = 'comfort'


class Multimedia(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мультимедиа'
        verbose_name_plural = 'Мультимедиа'
        db_table = 'multimedia'


class Other(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Опция',
        help_text='Пример (система помощи при парковке)',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прочее'
        verbose_name_plural = 'Прочее'
        db_table = 'other'


# Автомобиль на продажу
class Car(models.Model):
    new = models.BooleanField(
        verbose_name='Новый автомобиль или нет',
        help_text='Истина, если автомобиль новый, иначе Б/У. По умолчанию Б/У',
        default=False,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Марка',
        help_text='Марка автомобиля (например, BMW)',
        related_name='car_brand',
    )
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        verbose_name='Модель',
        help_text='Модель автомобиля (например, 5)',
        related_name='car_model',
    )
    generation = models.ForeignKey(
        Generation,
        on_delete=models.CASCADE,
        verbose_name='Поколение',
        help_text='Поколение автомобиля (например, 2019) ',
        related_name='car_generation',
    )
    modification = models.ForeignKey(
        Modification,
        on_delete=models.CASCADE,
        verbose_name='Модификация',
        help_text='Модификация автомобиля (например, 320i)',
        related_name='car_modification',
    )
    description = models.TextField(
        verbose_name="Описание автомобиля",
        blank=True,
        null=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='Цена автомобиля',
    )
    mileage = models.PositiveIntegerField(
        verbose_name='Пробег',
        help_text='Пробег автомобиля',
    )
    vin = models.CharField(
        max_length=17,
        verbose_name='VIN',
        help_text='VIN автомобиля',
        blank=True,
        null=True,
    )
    credit_from = models.PositiveIntegerField(
        verbose_name='Кредит от',
        help_text='Кредит от',
        blank=True,
        null=True,
    )
    secure = models.ManyToManyField(
        Secure,
        verbose_name='Безопасность',
        help_text='Безопасность автомобиля',
        related_name='car_secure',
    )
    exterior = models.ManyToManyField(
        Exterior,
        verbose_name='Экстерьер',
        help_text='Экстерьер автомобиля',
        related_name='car_exterior',
    )
    interior = models.ManyToManyField(
        Interior,
        verbose_name='Интерьер',
        help_text='Интерьер автомобиля',
        related_name='car_interior',
    )
    comfort = models.ManyToManyField(
        Comfort,
        verbose_name='Комфорт',
        help_text='Комфорт автомобиля',
        related_name='car_comfort',
    )
    multimedia = models.ManyToManyField(
        Multimedia,
        verbose_name='Мультимедиа',
        help_text='Мультимедиа автомобиля',
        related_name='car_multimedia',
    )
    other = models.ManyToManyField(
        Other,
        verbose_name='Прочее',
        help_text='Прочее автомобиля можно не заполнять',
        related_name='car_other',
        blank=True,
        null=True,
    )

    def get_first_image(self):
        image = self.car_images.first()
        return image.image.url

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.brand} {self.model} {self.generation} {self.modification}"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class CarImages(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Разрешение изображения должно быть 1920x1080',
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        help_text='Автомобиль, к которому относится изображение',
        related_name='car_images',
    )

    # валидация на разрешение изображения
    def clean(self):
        img = Image.open(self.image)
        width, height = img.size  # (width, height)
        # разрешение изображения должно быть больше 1920x1080 пикселей
        if width < 1920 or height < 1080:
            raise ValidationError('Разрешение изображения должно быть 1920x1080')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'car_images'
