from django.contrib.auth.forms import UserCreationForm
from .models import NewUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ('username', 'password1', 'password2', 'email')  # это поля формы, емейл по желанию)
