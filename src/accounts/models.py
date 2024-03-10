from django.contrib.auth.models import User
from django.utils import timezone


class MyUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Имя: {self.username}, email: {self.email}'
