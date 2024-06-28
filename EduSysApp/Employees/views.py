from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views import View

from EduSysApp.models import *


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'Employees/employees.html', {'employees': employees})

class AddEmployeeView(View):
    def post(self, request):
        # Получаем данные из POST-запроса
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')

        # Создание пользователя
        user = User.objects.create(
            username=username,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Получение группы "Преподаватель"
        group, created = Group.objects.get_or_create(name='Преподаватель')
        # Добавление пользователя в группу "Преподаватель"
        user.groups.add(group)

        employee = Employee.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            email=email
        )

        # Сохранение объекта в базе данных
        employee.save()

        return redirect('employees')

def employees_page(request):
    employees = Employee.objects.all()
    sorted_employees = None

    if request.method == 'POST':
        if 'sort_asc' in request.POST:
            sorted_employees = Employee.objects.order_by('last_name', 'first_name')
        elif 'sort_desc' in request.POST:
            sorted_employees = Employee.objects.order_by('-last_name', '-first_name')

    return render(request, 'Employees/employees.html', {'employees': employees, 'sorted_employees': sorted_employees})


class AddEmployeeView(View):
    def post(self, request):
        # Получаем данные из POST-запроса
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')

        # Создание пользователя
        user = User.objects.create(
            username=username,
            password=make_password(password),
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Получение группы "Преподаватель"
        group, created = Group.objects.get_or_create(name='Преподаватель')
        # Добавление пользователя в группу "Преподаватель"
        user.groups.add(group)

        employee = Employee.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            email=email
        )

        # Сохранение объекта в базе данных
        employee.save()

        return redirect('employees')

class EditEmployeeView(View):
    def post(self, request, employee_id):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        middle_name = request.POST.get('middle_name')
        email = request.POST.get('email')

        # Получение объекта Employee по его идентификатору
        employee = get_object_or_404(Employee, pk=employee_id)

        # Обновление данных сотрудника
        employee.first_name = first_name
        employee.last_name = last_name
        employee.middle_name = middle_name
        employee.phone_number = phone_number
        employee.email = email

        # Сохранение объекта в базе данных
        employee.save()
        return redirect('employees')


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    user = employee.user
    if user:
        user.delete()
    employee.delete()
    return redirect(reverse('employees'))