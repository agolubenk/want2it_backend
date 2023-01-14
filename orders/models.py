from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = (
        ('Ожидает ответа', 'Ожидает ответа'),
        ('Ответ направлен', 'Ответ направлен'),
        ('Пауза', 'Пауза'),
        ('Заявка закрыта', 'Заявка закрыта'),
    )
COUNTRY = (
        ('BY', 'Беларусь'),
        ('RU', 'Россия'),
        ('KZ', 'Казахстан'),
        ('US', 'США'),
        ('PL', 'Польша'),
        ('DE', 'Германия'),
        ('UK', 'Великобритания'),
        ('LT', 'Литва'),
        ('LV', 'Латвия'),
    )

class Order(models.Model):
    name = models.CharField("Имя", max_length=200)
    surname = models.CharField("Фамилия", max_length=200)
    telegram = models.URLField("Telegram", max_length=50, default='https://t.me/', unique=True)
    email = models.EmailField("E-mail", unique=True)
    company = models.CharField("Компания",max_length=50, default='--')
    country = models.CharField("Страна", max_length=500, choices=COUNTRY, default='Беларусь')
    phone = models.CharField("Телефон", max_length=18, unique=True)
    text = models.TextField("Сообщение")
    status = models.CharField("Статус", choices=STATUS, default='Ожидает ответа', max_length=50)
    order_date = models.DateTimeField("Дата заявки", default=timezone.now)
    last_date = models.DateTimeField('Последняя активность', blank=True, null=True)


    def publish(self):
        self.last_date = timezone.now()
        self.save()

    def __str__(self):
        return f' Заявка "{self.email}"'+f' ({self.order_date})'




