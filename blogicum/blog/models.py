from django.db import models
from blogicum.models import Base
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(Base):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации')
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    text = models.TextField(
        verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем — '
                   'можно делать отложенные публикации.'))
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Местоположение')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='categorys')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


class Category (Base):
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    description = models.TextField(
        verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, дефис и подчёркивание.'
        ))

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(Base):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
