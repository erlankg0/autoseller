from django.core.management.base import BaseCommand
from cars.models import Years


class Command(BaseCommand):
    help = 'Создание типов годов'

    def handle(self, *args, **options):
        years = [
            # YYYY-MM-DD
            '2010-01-01',
            '2011-01-01',
            '2012-01-01',
            '2013-01-01',
            '2014-01-01',
            '2015-01-01',
            '2016-01-01',
            '2017-01-01',
            '2018-01-01',
            '2019-01-01',

        ]
        for year in years:
            Years.objects.create(title=year)
            self.stdout.write(self.style.SUCCESS('Типы годов создан: %s' % year))
        self.stdout.write(self.style.SUCCESS('Типы годов созданы'))
