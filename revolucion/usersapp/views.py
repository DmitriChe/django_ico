from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
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
