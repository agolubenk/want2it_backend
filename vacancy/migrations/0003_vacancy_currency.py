# Generated by Django 4.1.5 on 2023-01-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_vacancy_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='currency',
            field=models.CharField(choices=[('usd', 'USD'), ('eur', 'EUR'), ('byn', 'BYN'), ('rub', 'RYB')], default='usd', max_length=500, verbose_name='Валюта'),
            preserve_default=False,
        ),
    ]
