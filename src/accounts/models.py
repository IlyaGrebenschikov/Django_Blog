from django.contrib.auth.models import User
from django.urls import reverse


class MyUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Имя: {self.username}, email: {self.email}'

    def get_absolute_url(self):
        return reverse("user-details", kwargs={"pk": self.pk})
