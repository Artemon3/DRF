from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from course.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    town = models.CharField(max_length=20, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Pay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата платежа')
    payment_amount = models.IntegerField(verbose_name='Сумма платежа', **NULLABLE)
    payment_method = models.IntegerField(verbose_name='Метод платежа', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.date}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'