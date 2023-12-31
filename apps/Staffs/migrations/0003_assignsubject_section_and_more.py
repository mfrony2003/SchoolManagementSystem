# Generated by Django 4.2.7 on 2023-12-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManagementSystemModules', '0006_section'),
        ('Staffs', '0002_assignsubject'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignsubject',
            name='section',
            field=models.ManyToManyField(to='SchoolManagementSystemModules.section'),
        ),
        migrations.RemoveField(
            model_name='assignsubject',
            name='studentclass',
        ),
        migrations.RemoveField(
            model_name='assignsubject',
            name='subjectname',
        ),
        migrations.AddField(
            model_name='assignsubject',
            name='studentclass',
            field=models.ManyToManyField(to='SchoolManagementSystemModules.studentclass'),
        ),
        migrations.AddField(
            model_name='assignsubject',
            name='subjectname',
            field=models.ManyToManyField(to='SchoolManagementSystemModules.subject'),
        ),
    ]
