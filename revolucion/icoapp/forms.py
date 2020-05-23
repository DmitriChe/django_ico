from django import forms
from bs4 import BeautifulSoup
import requests


class NumberofPagesForm(forms.Form):

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

    total_pages = get_number_of_pages()

    npages = forms.IntegerField(label=f'Введите число страниц от 1 до {total_pages}:')
