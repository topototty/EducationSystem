from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from EduSysApp.models import *

def study_group_list(request):
    groups = StudyGroup.objects.all()
    specializations = Specialization.objects.all()
    courses = Course.objects.all()
    return render(request, 'Groups/study_groups.html', {'specializations': specializations, 'courses': courses, 'groups' : groups})

class AddStudyGroupView(View):

    def post(self, request):
        group_number = request.POST.get('group_number')
        specialization_id = request.POST.get('specialization')
        course_id = request.POST.get('course')

        # Создание группы
        study_group = StudyGroup.objects.create(
            group_number=group_number,
            specialization_id=specialization_id,
            course_id=course_id
        )

        # Сохранение объекта в базе данных
        study_group.save()

        return redirect('groups')

class EditGroupView(View):
    def post(self, request, group_id):
        group_number = request.POST.get('group_number')
        specialization_id = request.POST.get('specialization')
        course_id = request.POST.get('course')

        group = get_object_or_404(StudyGroup, pk=group_id)

        group.group_number = group_number
        group.specialization_id = specialization_id
        group.course_id = course_id

        group.save()

        return redirect('groups')

class StudyGroupDelete(DeleteView):
    model = StudyGroup
    success_url = reverse_lazy('groups')
