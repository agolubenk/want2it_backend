# Generated by Django 4.1.5 on 2023-01-11 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('color', models.CharField(max_length=10, verbose_name='Цвет публикации')),
                ('text', models.TextField(verbose_name='Описание')),
                ('salary_from', models.IntegerField(verbose_name='Вилка от')),
                ('salary_to', models.IntegerField(verbose_name='Вилка до')),
                ('stack', models.CharField(max_length=500, verbose_name='Технологии')),
                ('benefits', models.TextField(verbose_name='Предложение и бонусы')),
                ('vacancy_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('activity', models.BooleanField(default=0, verbose_name='Активность')),
            ],
        ),
    ]
