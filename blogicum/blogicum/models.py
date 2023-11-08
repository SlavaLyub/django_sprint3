from django.db import models


class Base(models.Model):
    '''
    Абстрактная модель, добавляет флаг is_published=True
    добавляет строку с датой создания записи
    '''
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
