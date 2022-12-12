from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django_cleanup.signals import cleanup_post_delete


class File(models.Model):
    """ Модель файлов """
    
    file = models.FileField(
        upload_to='uploads/',
    )

    person = models.ForeignKey(
        verbose_name='водитель',
        to='person.Person',
        related_name='files',
        on_delete=models.CASCADE,
    )

    creator = UserForeignKey(
        auto_user_add=True,
        verbose_name="creator",
        related_name="files",
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'

    # def __str__(self):
    #     return self.file
