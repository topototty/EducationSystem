from django.contrib import admin
from django.urls import path, include
from EduSysApp.Grades import views as v
from .views import AddGradeView, EditGradeView

# from .views import AddLessonView, DeleteLesson, EditLessonView


from EduSysApp.views import *

urlpatterns = [
    path('grades/', v.grades_list, name='grades'),
    path('add_grade/', AddGradeView.as_view(), name='add_grade'),
    path('edit_grade/<int:grade_id>/', EditGradeView.as_view(), name='edit_grade'),
]
