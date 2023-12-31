# Generated by Django 4.2.7 on 2023-12-13 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0014_examtype_remove_result_mark_result_ctmark_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='ExamType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Students.examtype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='Student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Students.student'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StudentResult',
        ),
    ]
