# Generated by Django 5.0.6 on 2024-06-27 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_mailing_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='next_sent',
            field=models.DateTimeField(blank=True, default=models.DateTimeField(verbose_name='Дата и время первой отправки'), null=True, verbose_name='Дата и время следующей отправки'),
        ),
    ]