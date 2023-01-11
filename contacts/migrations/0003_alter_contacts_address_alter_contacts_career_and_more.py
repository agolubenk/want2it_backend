# Generated by Django 4.1.5 on 2023-01-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contacts_default_status_contacts_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(default='Минск, ', max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='career',
            field=models.URLField(default='https://career.habr.com/', verbose_name='Habr Career'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='facebook',
            field=models.URLField(default='https://facebook.com/', verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='instagram',
            field=models.URLField(default='https://instagram.com/', verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='linkedin',
            field=models.URLField(default='https://linkedin.com/in/', verbose_name='LinkedIn'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(default='+375', max_length=200, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='telegram',
            field=models.URLField(default='https://t.me/', verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='twitter',
            field=models.URLField(default='https://twitter.com/', verbose_name='Twitter'),
        ),
    ]
