from django.db import models

from cars.models import Car, Brand, Model, Generation, DriveUnit, Transmissions


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


class Gift(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название подарка',
        help_text='Подарок для клиента Trade-in',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подарок'
        verbose_name_plural = 'Подарки'
        ordering = ['-id']
        db_table = 'gifts'


class CallBack(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        help_text='Имя клиента',
    )  # имя клиента
    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        help_text='Номер телефона клиента',
    )  # номер телефона клиента

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'
        db_table = 'call_back'


class TradeInRequest(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        help_text='Имя клиента',
    )  # имя клиента
    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        help_text='Номер телефона клиента',
    )  # номер телефона клиента
    git = models.ForeignKey(
        Gift,
        on_delete=models.CASCADE,
        verbose_name='Подарок',
        help_text='Подарок для клиента',
    )  # подарок для клиента
    future_car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Будущий автомобиль',
        help_text='Будущий автомобиль',
    )  # будущий автомобиль
    current_car_brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Марка текущего автомобиля',
        help_text='Марка текущего автомобиля',
    )  # марка текущего автомобиля
    current_car_model = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        verbose_name='Модель текущего автомобиля',
        help_text='Модель текущего автомобиля',
    )  # модель текущего автомобиля
    current_car_year = models.IntegerField(
        verbose_name='Год выпуска текущего автомобиля',
        help_text='Год выпуска текущего автомобиля',
    )  # год выпуска текущего автомобиля
    current_car_transmission = models.ForeignKey(
        Transmissions,
        on_delete=models.CASCADE,
        verbose_name='Привод текущего автомобиля',
        help_text='Привод текущего автомобиля',
    )  # привод текущего автомобиля
    customer_price = models.IntegerField(
        verbose_name='Цена клиента',
        help_text='Цена клиента',
    )  # цена клиента
    credit = models.BooleanField(
        verbose_name='Кредит',
        help_text='Кредит',
    )  # кредит

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заявка на trade-in'
        verbose_name_plural = 'Заявки на trade-in'
        db_table = 'trade_in'


class CarReservation(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        help_text='Забронированный автомобиль',
    )  # автомобиль
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        help_text='Имя клиента',
    )  # имя клиента

    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        help_text='Номер телефона клиента',
    )  # номер телефона клиента
    date = models.DateField(
        verbose_name='Дата',
        help_text='Дата бронирования',
        auto_now_add=True,  # автоматически добавляет текущую дату
    )  # дата бронирования

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Бронирование автомобиля'
        verbose_name_plural = 'Бронирования автомобилей'
        db_table = 'car_reservation'


class Competitively(models.Model):
    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        help_text='Номер телефона клиента',
    )  # номер телефона клиента

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'Конкурентность'
        verbose_name_plural = 'Конкурентность'
        db_table = 'competitively'


# модель вопроса и номера телефона
class Question(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        help_text='Имя клиента',
    )  # имя клиента
    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона',
        help_text='Номер телефона клиента',
    )  # номер телефона клиента

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        db_table = 'question'
