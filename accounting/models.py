from django.conf import settings
from django.db import models
from django.utils import timezone


PARAMETRS = (
        ('Разработчики', 'Разработчики'),
        ('Администраторы (DBA, System)', 'Администраторы (DBA, System)'),
        ('Аналитики, Project- / Product- менеджеры', 'Аналитики, Project- / Product- менеджеры'),
        ('ML инженеры, AI разработчики', 'ML инженеры, AI разработчики'),
        ('Дизайнеры, UI/UX', 'Дизайнеры, UI/UX'),
        ('Системные инженеры, *Ops инженеры', 'Системные инженеры, *Ops инженеры'),
        ('Архитекторы', 'Архитекторы'),
        ('Тестировщики, QA', 'Тестировщики, QA'),
        ('Digital, маркетологи', 'Digital, маркетологи'),
        ('Менеджер по развитию бизнеса', 'Менеджер по развитию бизнеса'),
        ('HR-менеджеры, рекрутеры', 'HR-менеджеры, рекрутеры'),
        ('Прочие специальности', 'Прочие специальности'),
    )
CURRENCY = (
        ('$', 'USD'),
        ('€', 'EUR'),
        ('BYN', 'BYN'),
        ('₽', 'RYB'),
        ('₿', 'BTC'),
    )
VARIANTS = (
        ('год', 'Год'),
        ('месяц', 'Месяц'),
        ('вакансию', 'Вакансию'),
        ('команду', 'Команду'),
        ('сорсинг', 'Сорсинг'),
    )
ACTIVITY = (
        ('Неактивный', 'Неактивный'),
        ('Активный', 'Активный'),
    )
GRADE = (
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
    )
class Tarif(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)
    minimal_price = models.IntegerField("Минимальная цена", default=10)
    unit = models.CharField("Цена за", max_length=40, choices=VARIANTS)
    description = models.TextField("Описание")
    param_1 = models.CharField("Параметр 1", max_length=120)
    param_2 = models.CharField("Параметр 2", max_length=120)
    param_3 = models.CharField("Параметр 3", max_length=120)
    param_4 = models.CharField("Параметр 4", max_length=120)
    currency = models.CharField("Валюта", max_length=500, choices=CURRENCY)
    update_date = models.DateField("Дата обновления", default=timezone.now)
    activity = models.CharField('Активность', default='Неактивный', choices=ACTIVITY, max_length=20)


    def publish(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Тариф "{self.title}" ({self.activity})'



class Price(models.Model):
    parametrs = models.CharField("Направление", max_length=200, choices=PARAMETRS)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    grade = models.CharField("Грейд", max_length=500, choices=GRADE)
    salary = models.IntegerField("Цена", default=150)
    currency = models.CharField("Валюта", max_length=500, choices=CURRENCY, default='USD')
    price_date = models.DateField("Дата обновления", default=timezone.now)
    activity = models.CharField('Активность', default='Неактивный', choices=ACTIVITY, max_length=20)

    def publish(self):
        self.price_date = timezone.now()
        self._do_update()

    def __str__(self):
        return f'{self.parametrs} - {self.tarif} - {self.grade}'

    class Meta:
        unique_together = ('parametrs', 'tarif', 'grade')
