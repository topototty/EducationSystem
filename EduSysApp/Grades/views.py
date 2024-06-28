from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from EduSysApp.models import *


def grades_list(request):
    current_user = request.user
    current_employee = get_object_or_404(Employee, user=current_user)
    grades = Grade.objects.filter(employee=current_employee)

    employees = Employee.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()

    context = {
        'current_user': current_user,
        'employees': employees,
        'students': students,
        'subjects': subjects,
        'grades': grades
    }

    return render(request, 'Grades/grades.html', context)


class AddGradeView(View):
    def post(self, request):
        employee_id = request.POST.get('employee')
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade_value')
        grade_date = request.POST.get('grade_date')

        grade = Grade.objects.create(
            employee_id=employee_id,
            student_id=student_id,
            subject_id=subject_id,
            grade_value=grade_value,
            grade_date=grade_date
        )

        grade.save()

        return redirect('grades')


class EditGradeView(View):
    def post(self, request, grade_id):
        employee_id = request.POST.get('employee')
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade_value = request.POST.get('grade_value')
        grade_date = request.POST.get('grade_date')

        grade = get_object_or_404(Grade, pk=grade_id)

        grade.employee_id = employee_id
        grade.student_id = student_id
        grade.subject_id = subject_id
        grade.grade_value = grade_value
        grade.grade_date = grade_date

        grade.save()

        return redirect('grades')
