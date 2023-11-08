from django.db import models


class Base(models.Model):

    '''Абстр, добавляет is_pub=True и время создания записи'''

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено')

    class Meta:
        abstract = True
