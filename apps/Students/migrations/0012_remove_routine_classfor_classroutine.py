# Generated by Django 4.2.7 on 2023-12-11 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0011_alter_routine_end_time_alter_routine_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='classFor',
        ),
        migrations.CreateModel(
            name='ClassRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classFor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.class')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.routine')),
            ],
        ),
    ]
