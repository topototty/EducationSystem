# Generated by Django 5.0.2 on 2024-02-17 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('day_of_week_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_name', models.CharField(max_length=20, verbose_name='Название дня недели')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя сотрудника')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия сотрудника')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество сотрудника')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер телефона сотрудника')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта сотрудника')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_number', models.CharField(max_length=10, verbose_name='Номер группы')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=50, verbose_name='Название должности')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=50, verbose_name='Наименование роли')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=10, verbose_name='Номер аудитории')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization_name', models.CharField(max_length=100, verbose_name='Наименование специализации')),
                ('specialization_code', models.CharField(max_length=20, verbose_name='Код специализации')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100, verbose_name='Название предмета')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField(verbose_name='Время начала урока')),
                ('end_time', models.TimeField(verbose_name='Время окончания урока')),
                ('lesson_status', models.BooleanField(verbose_name='Статус урока')),
                ('day_of_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.dayofweek', verbose_name='День недели')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.employee', verbose_name='Сотрудник')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.group', verbose_name='Группа')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.room', verbose_name='Аудитория')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.subject', verbose_name='Предмет')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.position', verbose_name='Должность сотрудника'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('lesson_status', models.BooleanField(verbose_name='Статус запроса')),
                ('request_status', models.BooleanField(verbose_name='Статус запроса')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.employee', verbose_name='Сотрудник')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.lesson', verbose_name='Урок')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.specialization', verbose_name='Специализация'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя студента')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия студента')),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество студента')),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True, verbose_name='Номер телефона студента')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email студента')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.group', verbose_name='Группа')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_id', models.AutoField(primary_key=True, serialize=False)),
                ('grade_value', models.CharField(max_length=1, verbose_name='Значение оценки')),
                ('grade_date', models.DateField(verbose_name='Дата выставления оценки')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.student', verbose_name='Студент')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.subject', verbose_name='Предмет')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль пользователя')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.role', verbose_name='Роль пользователя')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduSysApp.user'),
        ),
    ]
