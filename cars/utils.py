import os


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
