from django.db import models

from cars.utils import directory_image_path, directory_image_path_vehicle, directory_image_path_cars
from cars.utils import engine_volume, car_year


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
        return self.title.year

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
    drive_unit = models.ManyToManyField(
        DriveUnit,
        verbose_name='Привод',
        help_text='Привод автомобиля',
        related_name='drive_unit_modifications',
    )
    body_type = models.ManyToManyField(
        BodyType,
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
        return self.title

    class Meta:
        verbose_name = 'Модификация'
        verbose_name_plural = 'Модификации'
        db_table = 'modification'


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
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='Цена автомобиля',
    )
    mileage = models.PositiveIntegerField(
        verbose_name='Пробег',
        help_text='Пробег автомобиля',
    )

    def save(self, *args, **kwargs):
        self.mileage = f'{self.mileage} км'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.modification.title

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class CarImages(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Изображение автомобиля',
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        help_text='Автомобиль, к которому относится изображение',
        related_name='car_images',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'car_images'
