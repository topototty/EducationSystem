from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .models import *
from .forms import RegistrationForm
from django.contrib.auth import logout as django_logout

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

from rest_framework import generics, viewsets


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']

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

            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
        else:
            messages.error(request, 'Заполните все поля формы.')
            return redirect('registration')
    else:
        form = RegistrationForm()

    return render(request, 'auth/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', user_id=user.id)
    return render(request, 'auth/login.html')


def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    employees = Employee.objects.all()
    lessons = Lesson.objects.all()
    user_groups = user.groups.values_list('name', flat=True)
    welcome_message = f"Добро пожаловать, {user.first_name} {user.last_name}"
    return render(request, 'Profile/profile.html', {
        'welcome_message': welcome_message,
        'lessons': lessons,
        'employees': employees,
        'user_groups': list(user_groups)
    })


def logout_view(request):
    django_logout(request)
    return redirect('login')
