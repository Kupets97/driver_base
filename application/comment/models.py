from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class Comment(models.Model):
    """ Модель комментариев """

    body = models.CharField(
        max_length=1000,
        verbose_name='комментарий',
    )
    person = models.ForeignKey(
        verbose_name='водитель',
        to='person.Person',
        on_delete=models.CASCADE,
    )
    
    creator = UserForeignKey(
        auto_user_add=True,
        verbose_name="пользователь", 
        related_name="creators"
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.body
