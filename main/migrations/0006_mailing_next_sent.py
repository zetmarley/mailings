# Generated by Django 5.0.6 on 2024-06-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mailing_job_id_alter_mailing_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='next_sent',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время следующей отправки'),
        ),
    ]