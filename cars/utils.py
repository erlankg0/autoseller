import os
import datetime


def directory_image_path(instance, filename):
    """
    Менеджер файлов
    instance -> Это класс
    filename имя файла
    """
    # логика изменения имя файла
    filename, ext = os.path.splitext(filename)
    filename = instance.title.lower() + ext
    return "brands/{0}".format(filename)


def directory_image_path_vehicle(instance, filename):
    """
    Менеджер файлов
    instance -> Это класс
    filename имя файла
    """
    # логика изменения имя файла
    filename, ext = os.path.splitext(filename)
    filename = instance.title.lower() + ext
    return "vehicles/{0}".format(filename)


def directory_image_path_cars(instance, filename):
    """
    Менеджер файлов
    instance -> Это класс
    filename имя файла
    """
    # логика изменения имя файла
    filename, ext = os.path.splitext(filename)
    filename = instance.title.lower() + ext
    return "cars/{0}".format(filename)


def engine_volume() -> tuple:  # -> tuple - указывает на тип возвращаемого значения
    volume = []
    for i in range(1, 5):
        for j in range(0, 10):
            volume.append((float(f"{i}.{j}"), float(f"{i}.{j}")))
    for i in range(5, 10):
        for j in range(0, 10):
            volume.append((float(f"{i}.{j}"), float(f"{i}.{j}")))
    return tuple(volume)  # Возвращаем кортеж из кортежей (1.0, 1.0), (1.1, 1.1) и т.д.


def car_year() -> tuple:
    year = []
    # get current year
    current_year = datetime.datetime.now().year
    for i in range(1950, current_year + 1):
        year.append((i, i))
    return tuple(year)
