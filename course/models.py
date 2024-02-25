from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course', **NULLABLE)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='courses', verbose_name='Картинка', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    url = models.URLField(max_length=200, verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
