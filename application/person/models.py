from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class Person(models.Model):
    """ Модель пользователя """
    
    first_name = models.CharField(
        max_length=64,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='Фамилия',
    )
    other_name = models.CharField(
        max_length=64,
        verbose_name='Отчество',
    )
    license = models.CharField(
        max_length=32,
        verbose_name='Номер водительского удостоверения',
        unique=True,
        db_index=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
    )
    raiting = models.ForeignKey(
            'raiting.Raiting', 
            on_delete=models.CASCADE,
            verbose_name='Рейтинг',
            related_name='persons',
    )
    
    creator = UserForeignKey(
        auto_user_add=True,
        verbose_name="creator id", 
        related_name="creator",
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'водитель'
        verbose_name_plural = 'водители'


    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f' Фамилия : {self.last_name or ""} , Имя : {self.first_name or ""} , Отчество : {self.other_name or ""} , Номер прав : {self.license or ""}'
