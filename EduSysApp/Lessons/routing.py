from django.contrib import admin
from django.urls import path, include
from EduSysApp.Lessons import views as v
from views import *
from .views import AddLessonView, DeleteLesson, EditLessonView


from EduSysApp.views import *

urlpatterns = [
    path('lessons/', v.lessons_list, name='lessons'),
    path('lessons_for_teacher/', v.teacher_lessons_list, name='lessons_for_teacher'),
    path('add_lesson/', AddLessonView.as_view(), name='add_lesson'),
    path('delete_lesson/<int:pk>/', DeleteLesson.as_view(), name='delete_lesson'),
    path('edit_lesson/<int:lesson_id>/', EditLessonView.as_view(), name='edit_lesson'),
]
