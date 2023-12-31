# Generated by Django 4.2.7 on 2023-12-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0013_result_alter_attendance_classins_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='Mark',
        ),
        migrations.AddField(
            model_name='result',
            name='CTMark',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='ExamMark',
            field=models.FloatField(default=0),
        ),
    ]
