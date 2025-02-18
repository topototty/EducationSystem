# Generated by Django 5.0.2 on 2024-02-20 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduSysApp', '0008_alter_grade_grade_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.employee', verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='request',
            name='lesson_status',
            field=models.BooleanField(verbose_name='Статус занятия'),
        ),
    ]
