from django.db import models
from blogicum.models import Base
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(Base):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete= models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete= models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Публикация'


class Category (Base):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)   

    class Meta:
        verbose_name = 'Тематическая категория'


class Location(Base):
    name = models.CharField(max_length=256)


    class Meta:
        verbose_name = 'Географическая метка'


# class User (models.Model):
#     ...

#     class Meta:
#         verbose_name = 'Пользователь'
