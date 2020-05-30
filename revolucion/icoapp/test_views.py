from django.test import Client, TestCase
from faker import Faker
from mixer.backend.django import mixer
from .models import Ico
from usersapp.models import NewUser


class OpenViewsTest(TestCase):
    def SetUp(self):
        self.client = Client()
        self.fake = Faker()

    def get_id(self):
        # получаю pk для первого объекта в БД
        icos = Ico.objects.all()
        id_ = 0
        for item in icos:
            id_ = item.id
            break

        return id_

    def test_logout_statuses(self):
        response = self.client.get('/')  # получаем объект ответа на get запрос клиента к корню сайта
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/parse/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/result/')
        self.assertEqual(response.status_code, 200)

        # проверка несуществующей страницы
        response = self.client.get('/no_page/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get(f'/detail/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

        response = self.client.get(f'/update/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

        response = self.client.get(f'/delete/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

    def test_user_login_statuses(self):
        # создаем простого пользователя:
        NewUser.objects.create_user(username='tuser', email='tuser@tuser.tu', password='tuser1234567')
        self.client.login(username='tuser', password='tuser1234567')

        response = self.client.get(f'/detail/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

        response = self.client.get(f'/update/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

        response = self.client.get(f'/delete/{self.get_id()}')
        self.assertEqual(response.status_code, 301)

        # self.client.logout()

    # def test_admin_login_statuses(self):
    #     pass











