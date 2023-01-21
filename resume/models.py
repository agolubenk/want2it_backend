from django.conf import settings
from django.db import models
from django.utils import timezone
import accounting.models

STATUS = (
        ('Ожидает ответа', 'Ожидает ответа'),
        ('Ответ направлен', 'Ответ направлен'),
        ('Пауза', 'Пауза'),
        ('Заявка закрыта', 'Заявка закрыта'),
    )
COUNTRY = (
        ('Беларусь', 'Беларусь'),
        ('Россия', 'Россия'),
        ('Казахстан', 'Казахстан'),
        ('США', 'США'),
        ('Польша', 'Польша'),
        ('Германия', 'Германия'),
        ('Великобритания', 'Великобритания'),
        ('Литва', 'Литва'),
        ('Латвия', 'Латвия'),
    )

class Order(models.Model):
    name = models.CharField("Имя", max_length=200)
    surname = models.CharField("Фамилия", max_length=200)
    telegram = models.CharField("Telegram", max_length=50, default='@', unique=True)
    email = models.EmailField("E-mail", unique=True)
    company = models.CharField("Компания", max_length=50, default='--')
    country = models.CharField("Страна", max_length=500, choices=COUNTRY, default='Беларусь')
    phone = models.CharField("Телефон", max_length=18, unique=True)
    text = models.TextField("Сообщение")
    status = models.CharField("Статус", choices=STATUS, default='Ожидает ответа', max_length=50)
    conformation = models.BooleanField("Согласие с правилами")
    order_date = models.DateTimeField("Дата заявки", default=timezone.now)
    last_date = models.DateTimeField('Последняя активность', blank=True, null=True)


    def publish(self):
        self.last_date = timezone.now()
        self.save()

    def __str__(self):
        return f' Заявка "{self.email}"'+f' ({self.order_date})'



