import csv

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from cities.models import City, PlanFact

DATA_ROOT = settings.BASE_DIR / 'data'


class Command(BaseCommand):
    help = (
        'Загрузка ингредиентов в базу данных из csv-файла '
        f'поместите файл в папку {DATA_ROOT} и запустите команду:'
        'python manage.py import_plan filename=\'имя файла\''
    )

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            default='data.csv',
            nargs='?',
            type=str
        )

    def handle(self, *args, **kwargs):
        input_file = kwargs['filename']
        with open(
            DATA_ROOT / input_file,
            newline='',
            encoding='utf8'
        ) as csv_file:
            try:
                file_content = csv.reader(csv_file)
                for row in file_content:
                    data_plan_fact = {
                        'year': int(row[0]),
                        'plan': int(row[2]),
                        'fact': int(row[3]),
                        'city': (City.objects
                                 .get_or_create(name=str(row[1]))[0]),
                    }
                    PlanFact.objects.get_or_create(**data_plan_fact)
            except FileNotFoundError:
                raise CommandError(
                    f'Файл {input_file} не найден в папке {DATA_ROOT}'
                )
            print(f'Данные из файла {input_file} успешно загружены')
