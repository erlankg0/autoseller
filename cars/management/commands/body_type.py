from django.core.management.base import BaseCommand
from cars.models import BodyType


class Command(BaseCommand):
    help = 'Создание типов транспорта'

    def handle(self, *args, **options):
        body_types = [
            'Седан',
            'Хэтчбек',
            'Хэтчбек 5 дв.',
            'Хэтчбек 3 дв.',
            'Универсал',
            'Кроссовер',
            'Внедорожник',
            'Спорткар'
            'Купе',
            'Кабриолет',
            'Лифтбек',
            'Минивэн',
            'Микроавтобус',
            'Фургон',
            'Пикап',
        ]
        for body_type in body_types:
            BodyType.objects.create(title=body_type)
            self.stdout.write(self.style.SUCCESS('Типы транспорта создан: %s' % body_type))
        self.stdout.write(self.style.SUCCESS('Типы транспорта созданы'))
