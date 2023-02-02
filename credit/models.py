from django.db import models
from cars.models import Car, Brand, Model, Generation


# заявка на кредит
class CreditRequest(models.Model):
    # марка автомобиля
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Марка автомобиля',
        related_name='credit_requests_brand',
    )
    # модель автомобиля
    model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        verbose_name='Модель автомобиля',
        related_name='credit_requests_model',
    )
    # автомобиль
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        related_name='credit_requests_car',
    )
    # имя клиента
    name = models.CharField(
        max_length=100,
        verbose_name='Имя клиента',
    )
    # первоначальный взнос
    initial_payment = models.IntegerField(
        verbose_name='Первоначальный взнос',
    )
    # срок кредита в месяцах
    credit_term = models.IntegerField(
        verbose_name='Срок кредита в месяцах',
    )
    # телефон клиента
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон клиента',
    )
    # проверен ли клиент
    is_checked = models.BooleanField(
        default=False,
        verbose_name='Проверен ли клиент',
        help_text='Если клиент проверен, то нажмите "На галочку"',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.car}'

    class Meta:
        verbose_name = 'Заявка на кредит'
        verbose_name_plural = 'Заявки на кредит'
        ordering = ['-id']
        db_table = 'credit_requests'


class TradeIn(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Имя клиента',
        help_text='Иванов Иван Иванович',
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон клиента',
        help_text='+7 (999) 999-99-99',
    )

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заявка на trade-in'
        verbose_name_plural = 'Заявки на trade-in'
        ordering = ['-id']
        db_table = 'trade_in_requests'
