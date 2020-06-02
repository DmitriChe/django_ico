from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import models
from .models import Ico, get_number_of_pages, parse_icos_to_db
from .forms import NumeroPagesForm
from django.core.mail import send_mail


from django.views.generic import View, ListView, UpdateView, CreateView, DetailView, DeleteView, FormView
from django.views.generic.base import TemplateView, ContextMixin
from .models import Ico


# Create your views here.
class MainTemplateView(TemplateView):
    template_name = 'icoapp/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'icoapp/about.html'


# права на парсин только у залогиненых пользователей
class IcoParse(LoginRequiredMixin, FormView):

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
    paginate_by = 5
    template_name = 'icoapp/result.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'результат обработки запроса'
        return context

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Ico.objects.filter(is_active=True)


class IcoDetailView(DetailView):
    model = Ico
    context_object_name = 'ico'
    template_name = 'icoapp/detail.html'


# права на измение записей об ico только у админа
class IcoUpdateView(UserPassesTestMixin, UpdateView):
    fields = '__all__'
    model = Ico
    template_name = 'icoapp/update.html'
    success_url = reverse_lazy('icoapp:result')

    # права на редактирование только у админа
    def test_func(self):
        return self.request.user.is_superuser

    # def form_valid(self, form):
    #     # self.request.user - текущий пользователь
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


# для удаления нужно быть админом
class IcoDeleteView(UserPassesTestMixin, DeleteView):
    model = Ico
    context_object_name = 'ico'
    template_name = 'icoapp/delete_confirm.html'
    success_url = reverse_lazy('icoapp:result')

    # права на удаление только у админа
    def test_func(self):
        return self.request.user.is_superuser

