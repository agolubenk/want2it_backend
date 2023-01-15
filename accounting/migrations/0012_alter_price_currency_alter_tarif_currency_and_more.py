# Generated by Django 4.1.5 on 2023-01-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_alter_price_unique_together_alter_price_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('€', 'EUR'), ('BYN', 'BYN'), ('₽', 'RYB'), ('₿', 'BTC')], default='USD', max_length=500, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('€', 'EUR'), ('BYN', 'BYN'), ('₽', 'RYB'), ('₿', 'BTC')], max_length=500, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='tarif',
            name='unit',
            field=models.CharField(choices=[('год', 'Год'), ('месяц', 'Месяц'), ('вакансию', 'Вакансию'), ('команду', 'Команду'), ('сорсинг', 'Сорсинг')], max_length=40, verbose_name='Цена за'),
        ),
    ]