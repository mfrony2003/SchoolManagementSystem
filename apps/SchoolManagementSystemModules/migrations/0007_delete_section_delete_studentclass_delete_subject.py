# Generated by Django 4.2.7 on 2023-12-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolManagementSystemModules', '0006_section'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
