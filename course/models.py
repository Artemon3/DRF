from django.db import models

from users.models import NULLABLE


# Create your models here.

class Lesson(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    url = models.URLField(max_length=200, verbose_name='Ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):

    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    lesson = models.ManyToManyField(Lesson, verbose_name='Урок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

