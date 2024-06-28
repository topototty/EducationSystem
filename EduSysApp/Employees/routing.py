from django.urls import path
from EduSysApp.Employees import views as v
from EduSysApp.Employees.views import *


urlpatterns = [
    path('employees/', v.employee_list, name='employees'),
    path('edit_employee/<int:employee_id>/', EditEmployeeView.as_view(), name='edit_employee'),
    path('add_employee/', AddEmployeeView.as_view(), name='add_employee'),
    path('delete_employee/<int:employee_id>/', delete_employee, name='delete_employee'),
]