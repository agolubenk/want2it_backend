# Generated by Django 4.1.5 on 2023-01-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='company',
            field=models.CharField(default='--', max_length=50, verbose_name='Компания'),
        ),
    ]
