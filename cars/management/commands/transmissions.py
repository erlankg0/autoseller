from django.core.management.base import BaseCommand
from cars.models import Transmissions


class Command(BaseCommand):
    help = 'Создание типов трансмиссий'

    def handle(self, *args, **options):
        transmissions = [
            'Механическая',
            'Автоматическая',
            'Роботизированная',
            'Вариатор',
            'Полуавтоматическая',

        ]
        for transmission in transmissions:
            Transmissions.objects.create(title=transmission)
            self.stdout.write(self.style.SUCCESS('Типы трансмиссий создан: %s' % transmission))
        self.stdout.write(self.style.SUCCESS('Типы трансмиссий созданы'))
