# Generated by Django 4.2.7 on 2023-12-21 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_gender_section_subject'),
        ('Students', '0018_attendance_section_attendance_staff_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.section'),
        ),
        migrations.AlterField(
            model_name='class',
            name='assigned_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.section'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.gender'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
