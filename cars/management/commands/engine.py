from django.core.management.base import BaseCommand
from cars.models import Engine, Fuel


class Command(BaseCommand):
    help = 'Создание типов двигателей'

    def handle(self, *args, **options):
        fuels = [
            'Бензин',
            'Дизель',
            'Газ',
            'Электричество',
        ]
        engines = [
            ('Бензиновый', 'Бензин'),
            ('Дизельный', 'Дизель'),
            ('Гибридный', 'Бензин'),
            ('Электро', 'Электричество'),
        ]

        for engine in engines:
            Engine.objects.create(title=engine[0], fuel=Fuel.objects.get_or_create(title=engine[1])[0])
            self.stdout.write(self.style.SUCCESS('Тип двигателя создан: %s' % engine[0]))
        self.stdout.write(self.style.SUCCESS('Типы двигателей созданы'))
