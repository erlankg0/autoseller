from django.core.management import BaseCommand
from cars.models import Brand


class Command(BaseCommand):
    help = "Создание брендов"

    def handle(self, *args, **options):
        brands = [
            "Kia",
            "Brilliance",
            "Citroen",
            "Ford",
            "Haima",
            "Lifan",
            "Peugeot",
            "UAZ",
            "Hyundai",
            "Changan",
            "Datsun",
            "Foton",
            "Haval",
            "Mazda",
            "Ravon",
            "Zotye",
            "Skoda",
            "Chery",
            "Donfeng",
            "GAC",
            "Honda",
            "Mitsubishi",
            "Renault",
            "Volkswagen",
            "CheryExeed",
            "DW Hower",
            "Geely",
            "JAC",
            "Nissan",
            "Ssang",
            "Toyota",
            "Chevrolet",
            "FAW",
            "Great Wall",
            "Lada",
            "Opel"
        ]
        for brand in brands:
            Brand.objects.get_or_create(title=brand)
        self.stdout.write(self.style.SUCCESS('Бренды успешно созданы'))
