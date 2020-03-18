from django.core.management.base import BaseCommand
from icoapp.models import Ico


class Command(BaseCommand):

    def handle(self, *args, **options):

        # выбор всех ico
        all_icos = Ico.objects.all()
        print('Это моя коза!')
        print(all_icos)
        print(type(all_icos))
        for item in all_icos:
            print(item.name)
            print(item.description)
            print(item.rating)
            print(type(item))

        print('End!')

        # Выбор одной категории
        ico = Ico.objects.get(name='test')
        print(ico)
        print(type(ico))

        # Выбор нескольких
        icos = Ico.objects.filter(rating=5.5)
        print(icos)
        print(type(icos))
        for item in icos:
            print(item.name, item.rating)

