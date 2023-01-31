from django.core.management import BaseCommand
from cars.models import Brand


class Command(BaseCommand):
    help = "Создание брендов"

    def handle(self, *args, **options):
        brands = [
            'Acura',
            'Alfa Romeo',
            'Aston Martin',
            'Audi',
            'Bentley',
            'BMW',
            'Mercedes-Benz',
            'Cadillac',
            'Chevrolet',
            'Toyota',
            'Volkswagen',
            'Volvo',
            'Lexus',
        ]
        for brand in brands:
            Brand.objects.get_or_create(title=brand)
        self.stdout.write(self.style.SUCCESS('Бренды успешно созданы'))
