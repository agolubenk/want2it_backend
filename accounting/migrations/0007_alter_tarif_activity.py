# Generated by Django 4.1.5 on 2023-01-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_alter_tarif_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarif',
            name='activity',
            field=models.BooleanField(choices=[(0, 'Неактивный'), (1, 'Активный')], default=0, verbose_name='Активность'),
        ),
    ]
