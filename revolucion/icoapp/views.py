from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Ico
from .forms import NumberofPagesForm
from django.core.mail import send_mail
from icoapp.models import Ico

from time import sleep
from bs4 import BeautifulSoup
import requests


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


# Create your views here.
def main_view(request):
    return render(request, 'icoapp/index.html')


def about_view(request):
    return render(request, 'icoapp/about.html')


def parse_view(request):

    if request.method == 'POST':  # если данные переданы методом пост, т.е. через форму, то
        form = NumberofPagesForm(request.POST)  # получаем форму и загружаем в нее данные POST запроса (в виде словаря)
        if form.is_valid():

            # получаем данные из формы
            num_of_pages = form.cleaned_data['npages']
            print(f'Получен запрос отпарсить первые {num_of_pages} страниц.')

            # парсим указанное число страниц и сохраняем в БД
            parse_icos_to_db(num_of_pages)

            all_icos = Ico.objects.all()
            # pprint.pprint(ico_data_dict)
            for item in all_icos:
                print(item.id, item.name, item.rating, item.url)

            send_mail(
                'Contact message',
                f'Запрос отпарсить {num_of_pages} страниц принят!',
                'from@example.com',
                ['email@email.ru'],
                fail_silently=True,  # если что не так - молчок!
            )
            # и после отправки письма делаем переход на начальную страницу
            return HttpResponseRedirect(reverse('icoapp:result'))
        else:
            return render(request, 'icoapp/about.html')

    else:
        form = NumberofPagesForm()
        return render(request, 'icoapp/parse.html', context={'form': form})


def result_view(request):
    icos = Ico.objects.all()  # берем все запси из модели Ico и передаем их в контексте в шаблон (т.е. на страницу)
    return render(request, 'icoapp/result.html', context={'icos': icos})



