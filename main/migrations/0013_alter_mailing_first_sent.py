# Generated by Django 5.0.6 on 2024-06-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_mailing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='first_sent',
            field=models.DateTimeField(verbose_name='Дата и время будущей отправки'),
        ),
    ]
