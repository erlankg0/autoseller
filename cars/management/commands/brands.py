from django.core.management import BaseCommand
from django.core.files import File
from cars.models import Brand
import json
import os
from autoseller.settings import BASE_DIR


class Command(BaseCommand):
    help = "Создание брендов"

    def handle(self, *args, **options):
        for item in [x for x in os.listdir('media/data/driver') if x.isupper()]:
            name = item.lower()
            img = name.lower()
            image = f'{BASE_DIR}\\media\\data\\driver\\{item}\\{item}.png'
            Brand.objects.get_or_create(title=name, icon=File(open(image, 'rb')))
        self.stdout.write(self.style.SUCCESS('Бренды успешно созданы'))
