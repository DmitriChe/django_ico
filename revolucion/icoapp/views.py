from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import models
from .models import Ico
from .forms import NumeroPagesForm
from django.core.mail import send_mail
from icoapp.models import Ico

from time import sleep
from bs4 import BeautifulSoup
import requests

from django.views.generic import View, ListView, UpdateView, CreateView, DetailView, DeleteView, FormView
from django.views.generic.base import TemplateView, ContextMixin
from .models import Ico


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
class MainTemplateView(TemplateView):
    template_name = 'icoapp/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'icoapp/about.html'


class IcoParse(FormView):

    form_class = NumeroPagesForm
    template_name = 'icoapp/parse.html'
    success_url = reverse_lazy('icoapp:result')

    def form_valid(self, form):
        num_of_pages = form.cleaned_data['npages']
        total_pages = get_number_of_pages()
        parse_icos_to_db(num_of_pages)
        return super().form_valid(form)


class ResultListView(ListView):
    model = Ico
    context_object_name = 'ico'
    template_name = 'icoapp/result.html'


class IcoDetailView(DetailView):
    model = Ico
    context_object_name = 'ico'
    template_name = 'icoapp/detail.html'


class IcoUpdateView(UpdateView):
    fields = '__all__'
    model = Ico
    template_name = 'icoapp/update.html'
    success_url = reverse_lazy('icoapp:result')


class IcoDeleteView(DeleteView):
    model = Ico
    context_object_name = 'ico'
    template_name = 'icoapp/delete_confirm.html'
    success_url = reverse_lazy('icoapp:result')

