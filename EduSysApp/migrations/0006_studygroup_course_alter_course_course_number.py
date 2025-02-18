# Generated by Django 5.0.2 on 2024-02-19 10:31

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduSysApp', '0005_remove_employee_position_delete_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Номер курса'),
        ),
    ]
