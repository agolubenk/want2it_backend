from django.conf import settings
from django.db import models
from django.utils import timezone

GRADE = (
        ('trainee', 'Trainee'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
        ('architect', 'Architect'),
        ('mentor', 'Mentor'),
        ('cto', 'CTO'),
        ('ceo', 'CEO'),
    )
CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('BYN', 'BYN'),
        ('RYB', 'RYB'),
    )

class Price(models.Model):
    title = models.CharField("Название", max_length=200)
    color = models.CharField("Цвет публикации", max_length=10)
    text = models.TextField("Описание")
    salary_from = models.IntegerField("Вилка от")
    salary_to = models.IntegerField("Вилка до")
    currency = models.CharField("Валюта", max_length=500, choices=CURRENCY)
    grade = models.CharField("Грейд", max_length=500, choices=GRADE)
    stack = models.CharField("Технологии", max_length=500)
    benefits = models.TextField("Предложение и бонусы")
    vacancy_date = models.DateField("Дата публикации", default=timezone.now)
    activity = models.BooleanField('Активность', default=0)
    hot = models.BooleanField('Продвижение', default=0)


    def publish(self):
        self.vacancy_date = timezone.now()
        self.save()

    def __str__(self):
        return f' "{self.title}"'+f' от {self.vacancy_date}'

    @property
    def stack_splitted(self):
        return self.stack.split(", ")


class Tarif(models.Model):
    title = models.CharField("Название", max_length=200)
    color = models.CharField("Цвет публикации", max_length=10)
    text = models.TextField("Описание")
    salary_from = models.IntegerField("Вилка от")
    salary_to = models.IntegerField("Вилка до")
    currency = models.CharField("Валюта", max_length=500, choices=CURRENCY)
    grade = models.CharField("Грейд", max_length=500, choices=GRADE)
    stack = models.CharField("Технологии", max_length=500)
    benefits = models.TextField("Предложение и бонусы")
    vacancy_date = models.DateField("Дата публикации", default=timezone.now)
    activity = models.BooleanField('Активность', default=0)
    hot = models.BooleanField('Продвижение', default=0)


    def publish(self):
        self.vacancy_date = timezone.now()
        self.save()

    def __str__(self):
        return f' "{self.title}"'+f' от {self.vacancy_date}'

    @property
    def stack_splitted(self):
        return self.stack.split(", ")



