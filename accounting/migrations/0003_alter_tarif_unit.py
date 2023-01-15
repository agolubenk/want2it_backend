# Generated by Django 4.1.5 on 2023-01-15 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_rename_text_tarif_description_remove_tarif_benefits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='unit',
            field=models.CharField(choices=[('y', 'Год'), ('m', 'Месяц'), ('v', 'Вакансию'), ('c', 'Команду'), ('s', 'Сорсинг')], max_length=40, verbose_name='Цена за'),
        ),
    ]
