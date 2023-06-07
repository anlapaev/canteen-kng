# Generated by Django 3.2.12 on 2023-06-07 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Создан'), (1, 'Собирается'), (2, 'Готов к выдаче'), (3, 'Выдан')], default=0),
        ),
    ]
