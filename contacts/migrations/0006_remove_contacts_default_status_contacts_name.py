# Generated by Django 4.1.5 on 2023-01-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_remove_contacts_telegramurl_alter_contacts_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='default_status',
        ),
        migrations.AddField(
            model_name='contacts',
            name='name',
            field=models.CharField(default='Неопознанный member', max_length=500, verbose_name='Фамилия Имя'),
        ),
    ]
