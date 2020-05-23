from django.urls import path
from icoapp import views  # импортируем вьюшки


app_name = 'icoapp'

# связываем вьюшки с адресами
urlpatterns = [
    path('', views.main_view, name='index'),
    # path('create/', views.create_post, name='create'),
    # path('post/<int:id>/', views.post, name='post')
]
