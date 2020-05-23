from django.urls import path
from icoapp import views  # импортируем вьюшки


app_name = 'icoapp'

# связываем вьюшки с адресами
urlpatterns = [
    path('', views.main_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('parse/', views.parse_view, name='parse'),
    path('result/', views.result_view, name='result'),
]
