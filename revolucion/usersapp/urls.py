from django.urls import path
from usersapp import views  # импортируем вьюшки


app_name = 'userapp'

# связываем вьюшки с адресами
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
]
