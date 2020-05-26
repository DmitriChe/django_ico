from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# добавим расширенного пользователя
class NewUser(AbstractUser):
    email = models.EmailField(unique=True)  # поле для уникального емейла
    is_author = models.BooleanField(default=False)  # может быть автором, т.е. создавать записи
