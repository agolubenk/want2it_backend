# Generated by Django 4.1.5 on 2023-01-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_country_alter_order_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='conformation',
            field=models.BooleanField(default=1, verbose_name='Согласие с правилами'),
            preserve_default=False,
        ),
    ]