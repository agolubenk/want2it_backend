# Generated by Django 4.1.5 on 2023-01-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последняя активность'),
        ),
    ]