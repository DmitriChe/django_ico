from django.core.management.base import BaseCommand
from icoapp.models import Ico
from bs4 import BeautifulSoup
from time import sleep
import requests
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        # получение максимального числа страниц с данными ico
        def get_number_of_pages(url='https://icobench.com/icos?'):

            html_doc = requests.get(url).text

            soup = BeautifulSoup(html_doc, 'html.parser')
            for num in soup.find_all('a', class_='num'):
                print(num)
            print('Все!')
            max_page_num = max([int(num.text) for num in soup.find_all('a', class_='num')])
            print('number of pages: {}'.format(max_page_num))
            return max_page_num

        # Парсинг данных с ico-сайта в базу данных
        def parse_icos_to_db(page_num):
            domain = 'https://icobench.com'
            url = '{}/icos?'.format(domain)

            # получаем число страниц на сайте с ico
            max_page_num = get_number_of_pages(url)

            # если запрошенное пользователем число страниц больше, чем есть на сайте, то корректируем это число.
            if page_num > max_page_num:
                page_num = max_page_num

            # предварительная очистка БД
            Ico.objects.all().delete()

            # парсим данные с ico-сайта в переменные, а затем в БД
            for i in range(page_num):
                sleep(1)
                next_page_url = '{}page={}'.format(url, i + 1)
                print('current page url: {}\n'.format(next_page_url))
                html_doc = requests.get(next_page_url).text
                soup = BeautifulSoup(html_doc, 'html.parser')
                ico_list = soup.find('div', class_='ico_list').find_all_next('tr')[1:-1]
                for item in ico_list:
                    ico_name = item.find('div', class_='content').a.text.strip()
                    ico_url = "{}{}".format(domain, item.find('div', class_='content').a.get('href'))
                    ico_description = item.find('p', class_='notranslate').text
                    ico_dates = item.find_all('td', class_='rmv')
                    ico_start_date = ico_dates[0].text
                    ico_end_date = ico_dates[1].text
                    ico_rating = item.find('div', class_='rate').text
                    print('{}: {}\n{}'.format(ico_name, ico_url, ico_description))
                    print('start date: {}\nend date: {}\nrating: {}\n'.format(ico_start_date, ico_end_date, ico_rating))

                    # Запуск на исполнение запроса на добавление данных в БД
                    Ico.objects.create(
                        name=ico_name,
                        description=ico_description,
                        starts=ico_start_date,
                        ends=ico_end_date,
                        rating=ico_rating,
                        url=ico_url
                    )

        total_pages = get_number_of_pages()

        num_of_pages = int(input('Сколько страниц нужно спарсить? (всего {} стр.): '.format(total_pages)))
        print('Получен запрос отпарсить первые {} страниц.'.format(num_of_pages))

        # парсим указанное число страниц и сохраняем в БД
        parse_icos_to_db(num_of_pages)

        all_icos = Ico.objects.all()
        # pprint.pprint(ico_data_dict)
        for item in all_icos:
            print(item.id, item.name, item.rating, item.url)



