# Generated by Django 5.0.6 on 2024-06-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_mailing_next_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='next_sent',
            field=models.DateTimeField(blank=True, default='<django.db.models.fields.DateTimeField>', null=True, verbose_name='Дата и время следующей отправки'),
        ),
    ]
