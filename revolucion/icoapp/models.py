from django.db import models
from usersapp.models import NewUser
from time import sleep
from bs4 import BeautifulSoup
import requests
from datetime import datetime


# получение максимального числа страниц с данными ico
def get_number_of_pages(url='https://icobench.com/icos?'):
    html_doc = requests.get(url).text

    soup = BeautifulSoup(html_doc, 'html.parser')
    for num in soup.find_all('a', class_='num'):
        print(num)
    print('Все!')
    max_page_num = max([int(num.text) for num in soup.find_all('a', class_='num')])
    print(f'number of pages: {max_page_num}')
    return max_page_num


# Парсинг данных с ico-сайта в базу данных
def parse_icos_to_db(page_num):
    domain = 'https://icobench.com'
    url = f'{domain}/icos?'

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
        next_page_url = f'{url}page={i + 1}'
        print(f'current page url: {next_page_url}\n')
        html_doc = requests.get(next_page_url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        ico_list = soup.find('div', class_='ico_list').find_all_next('tr')[1:-1]
        for item in ico_list:
            ico_name = item.find('div', class_='content').a.text.strip()
            ico_url = f"{domain}{item.find('div', class_='content').a.get('href')}"
            ico_description = item.find('p', class_='notranslate').text
            ico_dates = item.find_all('td', class_='rmv')
            ico_start_date = ico_dates[0].text
            ico_end_date = ico_dates[1].text
            ico_rating = item.find('div', class_='rate').text
            print(f'{ico_name}: {ico_url}\n{ico_description}')
            print(f'start date: {ico_start_date}\nend date: {ico_end_date}\nrating: {ico_rating}\n')

            # Запуск на исполнение запроса на добавление данных в БД
            Ico.objects.create(
                name=ico_name,
                description=ico_description,
                starts=ico_start_date,
                ends=ico_end_date,
                rating=ico_rating,
                url=ico_url
            )


# Create your models here.
class Ico(models.Model):
    # id создается автомитически
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField()
    starts = models.CharField(max_length=16)
    ends = models.CharField(max_length=16)
    rating = models.FloatField()
    url = models.URLField()
    # user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    # user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def count_ico_period(self):
        if self.starts == 'Unknown' or self.ends == 'Unknown':
            return 0
        else:
            date_start = datetime.strptime(self.starts, "%d %b %Y")
            date_end = datetime.strptime(self.ends, "%d %b %Y")
            delta = date_end - date_start
            return delta.days
