from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Создание пользователя'

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='0000', email='era@mail.com')
        self.stdout.write(self.style.SUCCESS('Пользователь создан: %s' % 'admin'))
