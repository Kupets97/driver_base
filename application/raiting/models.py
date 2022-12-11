from django.db import models


class Raiting(models.Model):
    """ Модель рейтинга пользователя """

    name = models.CharField(
        max_length=32,
        verbose_name='Категория',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинг'

    def __str__(self):
        return self.name
