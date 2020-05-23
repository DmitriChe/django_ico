from django.shortcuts import render
from .models import Ico


# Create your views here.
def main_view(request):
    icos = Ico.objects.all()  # берем все запси из модели Ico и передаем их в контексте в шаблон (т.е. на страницу)
    return render(request, 'icoapp/index.html', context={'icos': icos})
