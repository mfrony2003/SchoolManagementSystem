# Generated by Django 4.2.7 on 2023-12-30 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_religion'),
        ('Staffs', '0009_staff_dob_staff_nid_number_staff_phone_emergengy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='religion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.religion'),
            preserve_default=False,
        ),
    ]