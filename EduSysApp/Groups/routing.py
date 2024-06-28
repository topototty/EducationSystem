from django.urls import path

from EduSysApp.Groups import views
from EduSysApp.Groups.views import *

urlpatterns = [
    path('groups/', views.study_group_list, name='groups'),
    path('add_group/', AddStudyGroupView.as_view(), name='add_group'),
    path('delete_group/<int:pk>/', StudyGroupDelete.as_view(), name='delete_group'),
    path('edit_group/<int:group_id>/', EditGroupView.as_view(), name='edit_group'),
]