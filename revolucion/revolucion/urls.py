"""revolucion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # конструирование путей к вьюшкам по полученным урлам в адресной строке:
    path('', include('icoapp.urls', namespace='icoapp')),  # "переадресация" на файл urls приложения icoapp
    # path('users', include('usersapp.urls', namespace='userapp'))  # "переадресация" на файл urls приложения usersapp
    path('users/', include('usersapp.urls', namespace='users'))  # "переадресация" на файл urls приложения usersapp
]

# конструкция для того, чтобы джанго нормально находил папку с media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns