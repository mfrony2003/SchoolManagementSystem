# Generated by Django 4.2.7 on 2023-12-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0008_day_routine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='start_date',
        ),
        migrations.AddField(
            model_name='routine',
            name='end_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='routine',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
