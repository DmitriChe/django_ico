from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save  # сигнал на сразу после сохранения
from django.dispatch import receiver  # декоратор @receiver для обработки сигнала


# Create your models here.
# добавим расширенного пользователя
class NewUser(AbstractUser):
    email = models.EmailField(unique=True)  # поле для уникального емейла
    is_author = models.BooleanField(default=False)  # может быть автором, т.е. создавать записи


class Profile(models.Model):
    info = models.TextField(blank=True)  # необязательное поле для доп информации о пользователе
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)  # профиль связан с пользователем NewUser как 1 к 1


@receiver(post_save, sender=NewUser)
def create_profile(sender, instance, **kwargs):
    print('Создан профиль пользователя - по сигналу после его сохранения!')
    if not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)
