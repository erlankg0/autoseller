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

    # singelton pattern
    def save(self, *args, **kwargs):
        if Logo.objects.exists() and not self.pk:  # если логотип уже существует и это не редактирование
            raise ValidationError('Логотип уже существует')  # то выкидываем ошибку валидации (происходит в админке)
        return super().save(*args, **kwargs)

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
