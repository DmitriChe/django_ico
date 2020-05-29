from django.test import TestCase
from .models import Ico
from faker import Faker
from mixer.backend.django import mixer


# Create your tests here.
class IcoTestCase(TestCase):
    def test_count_ico_period(self):
        fake = Faker()
        ico1 = Ico.objects.create(name=fake.name(),
                                 description=fake.text(),
                                 starts='1 Jan 2020',
                                 ends='1  Jan 2021',
                                 rating=fake.pyfloat(positive=True),
                                 url=fake.url())

        ico2 = Ico.objects.create(name=fake.name(),
                                 description=fake.text(),
                                 starts='Unknown',
                                 ends='1  Jan 2021',
                                 rating=fake.pyfloat(positive=True),
                                 url=fake.url())

        self.assertEqual(ico1.count_ico_period(), 366)
        self.assertEqual(ico2.count_ico_period(), 0)


class IcoTestCaseFake(TestCase):
    def test_count_ico_period(self):
        ico1 = Ico.objects.create(name='Tycoon',
                                 description='Description of Tycoon',
                                 starts='1 Jan 2020',
                                 ends='1  Jan 2021',
                                 rating=4.9,
                                 url='http://tycoon.ru')

        ico2 = Ico.objects.create(name='Tycoon2',
                                 description='Description of Tycoon',
                                 starts='Unknown',
                                 ends='1  Jan 2021',
                                 rating=4.9,
                                 url='http://tycoon.ru')

        self.assertEqual(ico1.count_ico_period(), 366)
        self.assertEqual(ico2.count_ico_period(), 0)


class IcoTestCaseMixer(TestCase):
    def test_count_ico_period(self):
        ico1 = mixer.blend(Ico, starts='1 Jan 2020', ends='1  Jan 2021')

        ico2 = mixer.blend(Ico, starts='Unknown')

        ico3 = mixer.blend(Ico, ends='Unknown')

        self.assertEqual(ico1.count_ico_period(), 366)
        self.assertEqual(ico2.count_ico_period(), 0)
        self.assertEqual(ico3.count_ico_period(), 0)
