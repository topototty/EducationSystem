from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.IntegerField(verbose_name="Номер курса", validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f'{self.course_number}'
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Имя сотрудника")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия сотрудника")
    middle_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество сотрудника")
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name="Номер телефона сотрудника")
    email = models.EmailField(blank=True, null=True, verbose_name="Электронная почта сотрудника")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    specialization_name = models.CharField(max_length=100, verbose_name="Наименование специализации")
    specialization_code = models.CharField(max_length=20, verbose_name="Код специализации")

    def __str__(self):
        return f'{self.specialization_name}'

class StudyGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_number = models.CharField(max_length=10, verbose_name="Номер группы")
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name="Специализация")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", default=1)

    def __str__(self):
        return f'{self.group_number}'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="Имя студента")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия студента")
    middle_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество студента")
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name="Номер телефона студента")
    email = models.EmailField(blank=True, null=True, verbose_name="Email студента")
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name="Группа")

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.group}'

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, verbose_name="Номер аудитории")

    def __str__(self):
        return f'{self.room_number}'

class DayOfWeek(models.Model):
    day_of_week_id = models.AutoField(primary_key=True)
    day_name = models.CharField(max_length=20, verbose_name="Название дня недели")

    def __str__(self):
        return f'{self.day_name}'
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100, verbose_name="Название предмета")

    def __str__(self):
        return f'{self.subject_name}'

class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник", default='1')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    grade_value = models.IntegerField(verbose_name="Значение оценки", validators=[MinValueValidator(2), MaxValueValidator(5)])
    grade_date = models.DateField(verbose_name="Дата выставления оценки")

    def __str__(self):
        return f'{self.student} {self.subject} - {self.grade_value}'

class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name="Группа")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Аудитория")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    day_of_week = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Время начала урока")
    end_time = models.TimeField(verbose_name="Время окончания урока")
    lesson_status = models.BooleanField(verbose_name="Статус урока")

    def __str__(self):
        return f'{self.group} - {self.subject} - {self.day_of_week}'

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник", default=None)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    lesson_status = models.BooleanField(verbose_name="Статус занятия", default=True)
    request_status = models.BooleanField(verbose_name="Статус запроса", default=False)

    def str(self):
        return f'{self.lesson} - {self.lesson_status} - {self.request_status}'