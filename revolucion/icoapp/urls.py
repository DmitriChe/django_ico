from django.urls import path
from icoapp import views  # импортируем вьюшки
from rest_framework import routers
from .api_views import IcoViewSet

app_name = 'icoapp'

# router = routers.DefaultRouter()
# router.register(r'icos', IcoViewSet)

# связываем вьюшки с адресами
urlpatterns = [
    # path('', views.main_view, name='index'),
    path('', views.MainTemplateView.as_view(), name='index'),
    # path('about/', views.about_view, name='about'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    # path('parse/', views.parse_view, name='parse'),
    path('parse/', views.IcoParse.as_view(), name='parse'),
    # path('result/', views.result_view, name='result'),
    path('result/', views.ResultListView.as_view(), name='result'),
    path('detail/<int:pk>/', views.IcoDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.IcoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.IcoUpdateView.as_view(), name='update'),
]
