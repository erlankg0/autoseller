import json
import os
from json import JSONDecodeError
import codecs
from django.core.management.base import BaseCommand
from cars.models import Car, CarImages
from cars.models import Exterior, Interior, Comfort, Secure, Multimedia
from cars.models import Brand, Model, Generation, Modification
from cars.models import Engine, Transmissions, DriveUnit, BodyType, Fuel, Volume, Years
from django.core.files import File
from autoseller.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Fill data'

    def handle(self, *args, **options):
        brands = [x for x in os.listdir(f"{BASE_DIR}\\media\\data\\driver\\") if
                  x.isupper()]  # BRILLIANCE, KIA, LEXUS, ...

        for file in brands:
            brand_model = [x for x in os.listdir(f"{BASE_DIR}\\media\\data\\driver\\{file}") if
                           '.' not in x]  # brilliance, kia, lexus, ...
            print(brand_model)
            try:
                for current_models in brand_model:
                    current_model = [x for x in
                                     os.listdir(f"{BASE_DIR}\\media\\data\\driver\\{file}\\{current_models}")
                                     if x.endswith('.json')]
                    for json_file in current_model:

                        with open(
                                f"{BASE_DIR}\\media\\data\\driver\\{file}\\{current_models}\\{json_file}",
                                'r', encoding='cp1251') as f:
                            data = json.load(f)
                            try:
                                brand = Brand.objects.get_or_create(title=data["auto"]["brand"])[0]
                                model = Model.objects.get_or_create(title=data["auto"]["model"], brand=brand)[0]
                                generation = \
                                    Generation.objects.get_or_create(title=data["auto"]["generation"], model=model)[
                                        0]
                                fuel = Fuel.objects.get_or_create(title=data["auto"]["engine_type"])[0]
                                engine = \
                                    Engine.objects.get_or_create(title=data["auto"]["modification"], fuel=fuel)[0]
                                volume = Volume.objects.get_or_create(title=data["auto"]["volume"])[0]
                                transmissions = \
                                    Transmissions.objects.get_or_create(title=data["auto"]["transmission"])[
                                        0]
                                drive_unit = DriveUnit.objects.get_or_create(title=data["auto"]["drive_unit"])[0]
                                years = Years.objects.get_or_create(title=data["auto"]["year"])[0]
                                modification = Modification.objects.get_or_create(
                                    title=data["auto"]["modification"],
                                    model=model,
                                    engine=engine,
                                    power=data["auto"]["power"],
                                    volume=volume,
                                    fuel_consumption=data["auto"]["fuel_consumption"],
                                    acceleration=data["auto"]["acceleration"],
                                    max_speed=data["auto"]["max_speed"],
                                    body_type=BodyType.objects.get_or_create(title=data["auto"]["body_type"])[0],
                                    transmission=transmissions,
                                    drive_unit=drive_unit,
                                    year=years,
                                )[0]

                                car = Car.objects.create(
                                    new=False,
                                    brand=brand,
                                    model=model,
                                    generation=generation,
                                    modification=modification,
                                    price=data["auto"]["price"],
                                    credit_from=data["auto"]["credit_from"],
                                    mileage=0,
                                )
                                for item in data["auto"]["exterior"]:
                                    Exterior.objects.get_or_create(name=item)
                                for item in data["auto"]["interior"]:
                                    Interior.objects.get_or_create(name=item)
                                for item in data["auto"]["comfort"]:
                                    Comfort.objects.get_or_create(name=item)
                                for item in data["auto"]["secure"]:
                                    Secure.objects.get_or_create(name=item)
                                car.exterior.add(*Exterior.objects.filter(name__in=data["auto"]["exterior"]))
                                car.interior.add(*Interior.objects.filter(name__in=data["auto"]["interior"]))
                                car.comfort.add(*Comfort.objects.filter(name__in=data["auto"]["comfort"]))
                                car.secure.add(*Secure.objects.filter(name__in=data["auto"]["secure"]))
                                car.multimedia.add(*Multimedia.objects.filter(name__in=data["auto"]["multimedia"]))

                                for item in data["auto"]["images"][::-1]:
                                    full_path = os.path.join(
                                        'C:/Users/User/PycharmProjects/autoseller/media/data/driver/',
                                        item)
                                    with open(full_path, "rb") as f:
                                        CarImages.objects.create(
                                            car=car,
                                            image=File(f)
                                        )
                                self.stdout.write(
                                    self.style.SUCCESS(
                                        f'Successfully filled data for {model}/{data["auto"]["id"]}'))
                            except KeyError:
                                self.stdout.write(
                                    self.style.ERROR(f'Error in {model}/{data["auto"]["modification"]}'))
                                continue
                self.stdout.write(self.style.SUCCESS(f'Successfully filled data for {file}'))
            except JSONDecodeError:
                self.stdout.write(self.style.ERROR('Error in json file'))
                continue
