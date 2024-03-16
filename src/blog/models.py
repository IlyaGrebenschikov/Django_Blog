from django.db import models
from django.utils.timezone import now

from accounts.models import MyUser

# Create your models here.


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    author = models.ForeignKey(
        MyUser,
        verbose_name='Автор',
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    annotation = models.CharField('Аннотация', max_length=150)
    main_text = models.TextField('Статья')
    publication_date = models.DateTimeField(verbose_name="Дата публикации", default=now)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f'Заголовок - {self.title}, Пользователь - {self.author.username}'

