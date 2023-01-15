# Generated by Django 4.1.5 on 2023-01-15 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('telegram', models.URLField(default='https://t.me/', max_length=50, unique=True, verbose_name='Telegram')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('company', models.CharField(default='--', max_length=50, verbose_name='Компания')),
                ('country', models.CharField(choices=[('BY', 'Беларусь'), ('RU', 'Россия'), ('KZ', 'Казахстан'), ('US', 'США'), ('PL', 'Польша'), ('DE', 'Германия'), ('UK', 'Великобритания'), ('LT', 'Литва'), ('LV', 'Латвия')], default='Беларусь', max_length=500, verbose_name='Страна')),
                ('phone', models.CharField(max_length=18, unique=True, verbose_name='Телефон')),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('status', models.CharField(choices=[('Ожидает ответа', 'Ожидает ответа'), ('Ответ направлен', 'Ответ направлен'), ('Пауза', 'Пауза'), ('Заявка закрыта', 'Заявка закрыта')], default='Ожидает ответа', max_length=50, verbose_name='Статус')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заявки')),
                ('last_date', models.DateTimeField(blank=True, null=True, verbose_name='Последняя активность')),
            ],
        ),
    ]
