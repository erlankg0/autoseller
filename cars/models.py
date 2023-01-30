from django.db import models
from cars.utils import directory_image_path, directory_image_path_vehicle, directory_image_path_generation
from cars.utils import engine_volume


class Vehicle(models.Model):
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
        unique=True,
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


# Технические характеристики автомобиля
class TechnicalCharacteristics(models.Model):
    TRANSMISSION = (
        ('Автомат', 'Автомат'),
        ('Механика', 'Механика'),
        ('Робот', 'Робот'),
        ('Вариатор', 'Вариатор'),
        ('Типтроник', 'Типтроник'),
        ('Автомат-робот', 'Автомат-робот'),
    )
    FUEL = (
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Гибрид', 'Гибрид'),
        ('Электро', 'Электро'),
        ('Газ', 'Газ'),
        ('Газ-бензин', 'Газ-бензин'),
    )
    DRIVE_UNIT = (
        ('Передний', 'Передний'),
        ('Задний', 'Задний'),
        ('Полный', 'Полный'),
    )
    engine = models.CharField(
        max_length=50,
        verbose_name='Двигатель',
        help_text='Двигатель автомобиля (например, M57)',
    )
    fuel = models.CharField(
        max_length=50,
        verbose_name='Топливо',
        help_text='Топливо автомобиля (например, Бензин)',
        choices=FUEL,
    )
    transmission = models.CharField(
        max_length=50,
        verbose_name='Коробка передач',
        help_text='Коробка передач автомобиля (например, Автомат)',
        choices=TRANSMISSION,
    )
    drive_unit = models.CharField(
        max_length=50,
        verbose_name='Привод',
        help_text='Привод автомобиля (например, Полный)',
        choices=DRIVE_UNIT,
    )
    power = models.CharField(
        max_length=50,
        verbose_name='Мощность',
        help_text='Мощность автомобиля (например, 190 л.с.)',
    )
    volume = models.CharField(
        max_length=50,
        verbose_name='Объем',
        help_text='Объем автомобиля (например, 2.0)',
    )
    fuel_consumption = models.CharField(
        max_length=50,
        verbose_name='Расход топлива',
        help_text='Расход топлива автомобиля (например, 7.5)',
    )
    acceleration = models.CharField(
        max_length=50,
        verbose_name='Разгон',
        help_text='Разгон автомобиля (например, 7.5)',
    )
    max_speed = models.CharField(
        max_length=50,
        verbose_name='Максимальная скорость',
        help_text='Максимальная скорость автомобиля (например, 250)',
    )
    torque = models.CharField(
        max_length=50,
        verbose_name='Крутящий момент',
        help_text='Крутящий момент автомобиля (например, 250)',
    )

    def __str__(self):
        return f'{1} - {self.engine}'


class CarImages(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Изображение автомобиля',
    )
    used = models.BooleanField(
        verbose_name='Использовано или нет',
        help_text='Истина, если изображение использовано, иначе не использовано. По умолчанию не использовано',
        default=True,
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'car_images'


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
    technical_characteristics = models.ForeignKey(
        TechnicalCharacteristics,
        on_delete=models.CASCADE,
        verbose_name='Технические характеристики',
        help_text='Технические характеристики автомобиля',
        related_name='car_technical_characteristics',
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет',
        help_text='Цвет автомобиля (например, Черный)',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        help_text='Цена автомобиля (например, 1000000 рублей)',
    )
    mileage = models.PositiveIntegerField(
        verbose_name='Пробег',
        help_text='Пробег автомобиля (например, 1000000 км)',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание автомобиля',
    )
    image = models.ManyToManyField(
        CarImages,
        verbose_name='Изображения',
        help_text='Изображения автомобиля',
        related_name='car_image',
    )
    date = models.DateTimeField(
        verbose_name='Дата',
        help_text='Дата добавления автомобиля',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Марка: {self.brand}-Модельный ряд:{self.model}-Поколение:{self.generation}-Цвет:{self.color}-Цена:{self.price}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        db_table = 'car'
