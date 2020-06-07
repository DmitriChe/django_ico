from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse
from .forms import RegistrationForm
from .models import NewUser
from rest_framework.authtoken.models import Token


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


# Регистрация
class UserCreateView(CreateView):
    model = NewUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')


# профиль для генерации токена пользоватлю
class UserDetailView(DetailView):
    template_name = 'usersapp/profile.html'
    model = NewUser


def update_token(request):
    user = request.user
    if user.auth_token:
        # обновить токен, если был
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        # создать токен, если не было
        Token.objects.create(user=user)

    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))


def update_token_ajax(request):
    user = request.user
    if user.auth_token:
        # обновить токен, если был
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать токен, если не было
        token = Token.objects.create(user=user)

    return JsonResponse({'key': token.key})  # отдает токен в js как ответ сервера data для вставки в станицу
