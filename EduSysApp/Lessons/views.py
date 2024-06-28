from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from EduSysApp.models import *

def lessons_list(request):
    groups = StudyGroup.objects.all()
    employees = Employee.objects.all()
    rooms = Room.objects.all()
    subjects = Subject.objects.all()
    days_of_week = DayOfWeek.objects.all()

    lessons = Lesson.objects.all()
    return render(request, 'Lessons/lessons.html', {
        'lessons': lessons,
        'groups': groups,
        'employees': employees,
        'rooms': rooms,
        'subjects': subjects,
        'days_of_week': days_of_week,
    })

def teacher_lessons_list(request):

    current_user = request.user
    current_employee = get_object_or_404(Employee, user=current_user)
    lessons = Lesson.objects.filter(employee=current_employee)
    return render(request, 'Lessons/lessons_for_teacher.html', {'lessons': lessons})

class AddLessonView(View):
    def post(self, request):
        group_id = request.POST.get('group')
        employee_id = request.POST.get('employee')
        room_id = request.POST.get('room')
        subject_id = request.POST.get('subject')
        day_of_week_id = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        lesson_status = request.POST.get('lesson_status')

        # Создание урока
        lesson = Lesson.objects.create(
            group_id=group_id,
            employee_id=employee_id,
            room_id=room_id,
            subject_id=subject_id,
            day_of_week_id=day_of_week_id,
            start_time=start_time,
            end_time=end_time,
            lesson_status=lesson_status
        )

        # Сохранение объекта в базе данных
        lesson.save()

        return redirect('lessons')


class EditLessonView(View):
    def post(self, request, lesson_id):
        group_id = request.POST.get('group')
        employee_id = request.POST.get('employee')
        room_id = request.POST.get('room')
        subject_id = request.POST.get('subject')
        day_of_week_id = request.POST.get('day_of_week')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        lesson_status = request.POST.get('lesson_status')

        lesson = get_object_or_404(Lesson, pk=lesson_id)

        lesson.group_id = group_id
        lesson.employee_id = employee_id
        lesson.room_id = room_id
        lesson.subject_id = subject_id
        lesson.day_of_week_id = day_of_week_id
        lesson.start_time = start_time
        lesson.end_time = end_time
        lesson.lesson_status = lesson_status

        lesson.save()

        return redirect('lessons')
class DeleteLesson(DeleteView):
    model = Lesson
    success_url = reverse_lazy('lessons')