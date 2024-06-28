from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from EduSysApp.models import *


def request_list(request):
    requests = Request.objects.all()
    employees = Employee.objects.all()
    lessons = Lesson.objects.all()
    return render(request, 'Requests/requests.html', {'requests': requests, 'lessons': lessons, 'employees': employees})


def request_list_for_employee(request):
    current_user = request.user
    current_employee = Employee.objects.get(user=current_user)
    requests = Request.objects.filter(employee=current_employee)
    lessons = Lesson.objects.all()
    return render(request, 'Requests/requests_for_employee.html',
                  {'requests': requests, 'lessons': lessons, 'current_employee': current_employee})


class AddRequestView(View):
    def post(self, request):
        employee_id = request.POST.get('employee')
        lesson_id = request.POST.get('lesson')
        lesson_status = request.POST.get('lesson_status')

        request_obj = Request.objects.create(
            employee_id=employee_id,
            lesson_id=lesson_id,
            lesson_status=lesson_status,
        )

        request_obj.save()

        return redirect('requests_for_employee')


class EditRequestView(View):
    def post(self, request, request_id):
        employee_id = request.POST.get('employee')
        lesson_id = request.POST.get('lesson')
        lesson_status = request.POST.get('lesson_status')
        request_status = request.POST.get('request_status')

        request_obj = get_object_or_404(Request, pk=request_id)

        request_obj.employee_id = employee_id
        request_obj.lesson_id = lesson_id
        request_obj.lesson_status = lesson_status
        request_obj.request_status = request_status

        request_obj.save()

        if request_status == '1':
            lesson_obj = request_obj.lesson
            lesson_obj.lesson_status = lesson_status
            lesson_obj.save()

        return redirect('requests')
