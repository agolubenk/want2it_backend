from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import F

POSITION = (
        ('Рекрутер', 'Рекрутер'),
        ('Директор', 'Директор'),
        ('Организация', 'Организация'),
        ('Техподдержка', 'Техподдержка'),
    )
class Contacts(models.Model):
    title = models.CharField("Должность", max_length=500, choices=POSITION, default='Рекрутер')
    name = models.CharField("Фамилия Имя", max_length=500, default='Неопознанный member')
    telegram = models.CharField("Telegram",max_length=200)
    facebook = models.URLField("Facebook",max_length=200, default='https://facebook.com/')
    instagram = models.URLField("Instagram",max_length=200, default='https://instagram.com/')
    career = models.URLField("Habr Career",max_length=200, default='https://career.habr.com/')
    twitter = models.URLField("Twitter",max_length=200, default='https://twitter.com/')
    linkedin = models.URLField("LinkedIn",max_length=200, default='https://linkedin.com/in/')
    phone = models.CharField("Телефон",max_length=200, default='+375')
    email = models.EmailField("Email",max_length=200, unique=True)
    address = models.CharField("Адрес",max_length=200, default='Минск, ')

    def __str__(self):
        return self.title
