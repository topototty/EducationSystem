from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from EduSysApp.models import *


def students_list(request):
    groups = StudyGroup.objects.all()
    students = Student.objects.all()
    return render(request, 'Students/students.html', {'groups': groups, 'students': students})

class AddStudentView(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        group_id = request.POST.get('group')

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            email=email,
            group_id=group_id
        )

        # Сохранение объекта в базе данных
        student.save()

        return redirect('students')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')

class EditStudentView(View):
    def post(self, request, student_id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        group_id = request.POST.get('group')

        student = get_object_or_404(Student, pk=student_id)

        student.first_name = first_name
        student.last_name = last_name
        student.middle_name = middle_name
        student.phone_number = phone_number
        student.email = email
        student.group_id = group_id

        student.save()

        return redirect('students')

