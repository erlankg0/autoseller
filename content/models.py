from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models


class Phone(models.Model):
    number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        help_text='Номер телефона в формате +7 (999) 999-99-99)',
        unique=True
    )  # номер телефона в формате +7 (999) 999-99-99 РФ

    def clean_number(self):
        number = self.cleaned_data['number']
        if not number.startswith('+7'):
            raise ValidationError('Номер должен начинаться с +7')
        return number

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['number']


class Address(models.Model):
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        help_text='Адрес компании',
        unique=True
    )  # адрес компании

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Email(models.Model):
    email = models.EmailField(
        verbose_name='Email',
        help_text='Email компании',
        unique=True
    )  # email компании

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email'


class Logo(models.Model):
    logo = models.ImageField(
        verbose_name='Логотип',
        help_text='Логотип компании',
        upload_to='logo'
    )  # логотип компании

    def __str__(self):
        return f'Логотип {self.pk}'

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'


class WorkTime(models.Model):
    time = models.CharField(
        max_length=255,
        verbose_name='Время работы',
        help_text='Время работы компании',
        unique=True
    )  # время работы компании

    def __str__(self):
        return self.time

    def save(self, *args, **kwargs):
        if WorkTime.objects.exists() and not self.pk:  # если время работы уже существует и это не редактирование
            raise ValidationError('Логотип уже существует')  # то выкидываем ошибку валидации (происходит в админке)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'


class TechCenter(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        help_text='Название услуги (например: "Ремонт техники кузова")',
        unique=True,
    )  # название услуги (например: "Ремонт техники кузова")
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание услуги',
    )  # описание услуги

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['title']
        db_table = 'tech_center'


class Title(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Заголовок страницы",
        unique=True
    )  # заголовок страницы

    # singelton pattern
    def save(self, *args, **kwargs):
        if Title.objects.exists() and not self.pk:
            raise ValidationError('Заголовок уже существует')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        db_table = 'title'


class Whatsapp(models.Model):
    number = models.CharField(
        max_length=14,
        verbose_name='Номер',
        unique=True,
        help_text='Номер телефона для WhatsApp (например: 79999999999) без +7 Максимум можно добавить только один номер'
    )  # номер телефона для WhatsApp

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        if Whatsapp.objects.exists() and not self.pk:
            return
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Номер WhatsApp'
        verbose_name_plural = 'Номера WhatsApp'
        db_table = 'whatsapp'


class HowToGo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        help_text='Название (например: "Как добраться")',
        unique=True
    )  # название (например: "Как добраться")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Как добраться'
        verbose_name_plural = 'Как добраться'
        ordering = ['title']
        db_table = 'how_to_go'


class Best(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        help_text='Заголовок (например: "Лучший")',
        unique=True
    )  # заголовок (например: "Лучший")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Лучший'
        verbose_name_plural = 'Лучший'
        ordering = ['title']
        db_table = 'best'


class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        help_text='Заголовок (например: "О нас")',
        unique=True
    )  # заголовок (например: "О нас")
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание',
    )  # описание
    best_title = models.CharField(
        max_length=255,
        verbose_name='Заголовок лучшего',
        help_text='Заголовок лучшего (например: "Лучший")',
    )  # заголовок лучшего (например: "Лучший")
    best_item = models.ManyToManyField(
        Best,
        verbose_name='Лучший',
        help_text='Лучший',
    )  # лучший

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['title']
        db_table = 'about'


class Images(models.Model):
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение',
        help_text='Изображение',
    )  # изображение
    about = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        verbose_name='О нас',
        help_text='О нас',
        related_name='images'
    )  # о нас

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['image']
        db_table = 'images'


class DNS(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='URL сайта',
        help_text='URL сайта (например: "https://example.com")',
        unique=True
    )  # URL сайта

    def save(self, *args, **kwargs):
        if DNS.objects.exists() and not self.pk:
            return
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'URL сайта'
        verbose_name_plural = 'URL сайта'
        db_table = 'dns'


class Banner(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок',
        help_text='Заголовок баннера',
        unique=True
    )  # заголовок баннера
    subtitle = models.CharField(
        max_length=255,
        verbose_name='Подзаголовок',
        help_text='Подзаголовок баннера',
        unique=True
    )  # подзаголовок баннера

    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание баннера',
    )  # описание баннера
    car_image = models.ImageField(
        upload_to='banners/',
        verbose_name='Изображение',
        help_text='Изображение баннера',
    )  # изображение баннера
    car_image_2 = models.ImageField(
        upload_to='banners/',
        verbose_name='Изображение 2',
        help_text='Изображение баннера 2',
    )  # изображение баннера 2
    car_image_3 = models.ImageField(
        upload_to='banners/',
        verbose_name='Изображение 3',
        help_text='Изображение баннера 3',
    )  # изображение баннера 3

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        db_table = 'banner'


class Banks(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название банка',
        help_text='Название банка',
        unique=True
    )  # название банка
    image = models.ImageField(
        upload_to='banks/',
        verbose_name='Изображение логотип банка',
        help_text='Размер изображения должен быть минимум 200px по ширине и максимум 100px по высоте',
    )  # изображение банка

    def __str__(self):
        return self.title

    def clean(self):
        # Валидация размера изображения мин и макс ширина 200px и высота максимум 100px
        if self.image:
            img = Image.open(self.image)
            width, height = img.size
            if width < 200 or height > 100:
                raise ValidationError(
                    'Размер изображения должен быть минимум 200px по ширине и максимум 100px по высоте')

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        db_table = 'banks'


class Color(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название цвета',
        help_text='Название цвета',
        unique=True
    )  # название цвета
    color = models.CharField(
        max_length=255,
        verbose_name='Цвет',
        help_text='Цвет',
        unique=True
    )  # цвет

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        db_table = 'color'


class Favicon(models.Model):
    favicon = models.ImageField(
        upload_to='favicon/',
        verbose_name='Иконка',
        help_text='Иконка',
    )  # иконка

    def get_last_favicon(self):
        return Favicon.objects.last()

    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'
        db_table = 'favicon'


class Tag(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название тега',
        help_text='Название тега',
        unique=True
    )  # название тега
    description = models.CharField(
        max_length=50,
        verbose_name='Описание тега',
        help_text='Описание тега (до 50 символов)',
        unique=True
    )  # описание тега

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        db_table = 'tag'


class VK(models.Model):
    url = models.URLField(
        verbose_name='Ссылка на группу',
        help_text='Ссылка на группу',
        unique=True
    )  # ссылка на группу

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Группа ВК'
        verbose_name_plural = 'Группы ВК'
        db_table = 'vk'
