# Generated by Django 4.2.7 on 2023-12-07 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_class_student_student_code_classstudent_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Students.class'),
            preserve_default=False,
        ),
    ]