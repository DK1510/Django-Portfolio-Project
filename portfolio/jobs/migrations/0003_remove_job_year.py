# Generated by Django 4.2.6 on 2023-11-03 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='year',
        ),
    ]
