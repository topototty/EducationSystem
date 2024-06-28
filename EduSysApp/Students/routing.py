from django.urls import path

from EduSysApp.Students import views
from EduSysApp.Students.views import *

urlpatterns = [
    path('students/', views.students_list, name='students'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('delete_student/<int:pk>/', StudentDelete.as_view(), name='delete_student'),
    path('edit_student/<int:student_id>/', EditStudentView.as_view(), name='edit_student'),
]