from django.urls import path
from usersapp import views  # импортируем вьюшки
from django.contrib.auth.views import LogoutView


app_name = 'userapp'

# связываем вьюшки с адресами
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
]