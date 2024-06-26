# Generated by Django 5.0.6 on 2024-06-18 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_sent', models.DateTimeField(default=datetime.datetime.now)),
                ('periodicity', models.IntegerField(default=7, verbose_name='периодичность')),
                ('status', models.CharField(default='created', max_length=30, verbose_name='статус')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
