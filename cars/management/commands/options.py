from cars.models import Exterior, Interior, Secure, Comfort, Multimedia, Other
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Создание базовых опций'

    def handle(self, *args, **options):
        exteriors = [
            'Диски 16',
            'Диски 17',
            'Диски 18',
            'Металлик',
            'Полностью светодиодная задняя оптика',
            'Светодиодная передняя оптика',
            'LED фары',
            'LED ходовые огни',
            'LED фары и ходовые огни',
            'LED фары и ходовые огни с дневными ходовыми огнями',
            'LED фары и ходовые огни с дневными ходовыми огнями и поворотами',
            'Xenon фары',
            'Xenon фары и ходовые огни',
            'Xenon фары и ходовые огни с дневными ходовыми огнями и поворотами',
            'Автоматический датчик дождя',
            'Автоматический датчик света и дождя с автоматическим включением фар',
            'Антенна «Плавник акулы»',
            'Легкосплавные колесные диски, шины 235/45 R18',
            'Легкосплавные колесные диски, шины 235/50 R18',
            'Ручки дверей с хромированной накладкой',
            'Светодиодные фары',
            'Светодиодные фары и ходовые огни',
            'Омыватели фар',
        ]
        interiors = [
            'Кожаный салон',
            'Кожаный салон с электрорегулировкой водителя и пассажира с памятью',
            'Кожаный руль',
            'Алькантара',
            'Алькантара с электрорегулировкой водителя',
            'Алькантара с электрорегулировкой водителя и пассажира',
            'Кожаный салон с противоскольжением',
            'Кожаный салон с противоскольжением и электрорегулировкой водителя',
        ]
        security = [
            'Антиблокировочная система (ABS)',
            'Антипробуксовочная система (ASR)',
            'Система распределения тормозного усилия (EBD)',
            'Система контроля давления в шинах (TPMS)',
            'Система контроля давления в шинах (TPMS) с датчиками в шинах',
            'Система курсовой устойчивости (VSC+)',
            'Антипробуксовочная система (TRC)',
            'Система помощи при подъеме по склону (HAC)',
        ]
        comfort = [
            'Климат-контроль',
            'Климат-контроль с двумя зонами',
            'Климат-контроль с двумя зонами и регулировкой воздуха в салоне',
            'Мультифункциональное рулевое колесо с кожаной обивкой (комбинация из натуральной и синтетической кожи)',
            'Передние и задние стеклоподъемники с функцией «Auto»',
            'Передние и задние стеклоподъемники с функцией «One Touch»',
            'Регулировка рулевой колонки по вылету и по наклону',
        ]
        multimedia = [
            'Аудиосистема с CD-проигрывателем, 6 динамиками, 2 выходами на наушники и AUX-входом',
            'USB-разъем для воспроизведения медиафайлов и зарядки мобильных устройств на центральной консоли',
            'Аудио-разъем (AUX)',
            'Аудиосистема премиум класса JBL с поддержкой CD/MP3/WMA/AAC/WAV/FLAC/ALAC',
            '9 динамиков аудиосистемы (включая сабвуфер)',
            'Мультимедийная система CY"17" c "8" цветным дисплеем и навигационной системой',
            'CARPLAY',
            'ANDROID AUTO',
            'Система поддержки вождения по тонкой металлической проволоке (LDWS)',
        ]

        for exterior in exteriors:
            exterior_ = Exterior.objects.create(name=exterior)
            self.stdout.write(self.style.SUCCESS(f'Экстерьер "{exterior_}" создан'))
        self.stdout.write(self.style.SUCCESS('Экстерьеры созданы'))

        for interior in interiors:
            interior_ = Interior.objects.create(name=interior)
            self.stdout.write(self.style.SUCCESS(f'Интерьер "{interior_}" создан'))
        self.stdout.write(self.style.SUCCESS('Интерьеры созданы'))

        for secure in security:
            security_ = Secure.objects.create(name=secure)
            self.stdout.write(self.style.SUCCESS(f'Безопасность "{security_}" создана'))
        self.stdout.write(self.style.SUCCESS('Безопасности созданы'))

        for comfort_ in comfort:
            comfort__ = Comfort.objects.create(name=comfort_)
            self.stdout.write(self.style.SUCCESS(f'Комфорт "{comfort__}" создан'))
        self.stdout.write(self.style.SUCCESS('Комфорты созданы'))

        for multimedia_ in multimedia:
            multimedia__ = Multimedia.objects.create(name=multimedia_)
            self.stdout.write(self.style.SUCCESS(f'Мультимедиа "{multimedia__}" создана'))
        self.stdout.write(self.style.SUCCESS('Мультимедиа созданы'))

        self.stdout.write(self.style.SUCCESS('Создание завершено'))
