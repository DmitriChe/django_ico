from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm
from .models import NewUser


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


# Регистрация
class UserCreateView(CreateView):
    model = NewUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')
